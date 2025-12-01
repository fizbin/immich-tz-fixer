from __future__ import annotations

import argparse
import logging
import pathlib
import sys
from collections.abc import Iterable
from datetime import datetime, time, timedelta, tzinfo
from uuid import UUID

import dateutil
import exiftool  # type: ignore

import immich_tz_fixer  # important: use only for __version__
from immich_client import UNSET, AuthenticatedClient
from immich_client.api.assets import get_asset_info, update_asset
from immich_client.api.search import search_assets
from immich_client.api.tags import get_all_tags
from immich_client.models import MetadataSearchDto
from immich_client.models.asset_response_dto import AssetResponseDto
from immich_client.models.exif_response_dto import ExifResponseDto
from immich_client.models.update_asset_dto import UpdateAssetDto

"""
Basic CLI entrypoint for immich_tz_fixer.

Provides a `run` function that can be used as an entrypoint for testing or packaging.
"""

logger = logging.getLogger(__name__)


class ImmichClientError(Exception):
    """Unexpected error from the Immich API server"""

    pass


def _parse_args(argv: None | Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="immich-tz-fixer",
        description="Adjust immich asset time zones based on local file metadata.",
    )
    parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="Immich API endpoint (e.g. 'https://myphotos.example.com/api')",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        required=True,
        help="Immich API key for authentication",
    )
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version=f"immich-fixer {immich_tz_fixer.__version__}",
        help="Show program version and exit.",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        dest="dry_run",
        action="store_true",
        help="Print actions that would be taken without modifying anything.",
    )
    parser.add_argument(
        "--timezone",
        type=str,
        help="Assume/overwrite given timezone (e.g. 'America/New_York')",
    )
    parser.add_argument(
        "--before",
        type=str,
        help="Only process immich assets before this date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--after",
        type=str,
        help="Only process immich assets after this date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--model",
        type=str,
        help="Only find photos taken with this model (e.g. 'DMC-GX85')",
    )
    parser.add_argument(
        "--tag",
        type=str,
        dest="tags",
        action="append",
        default=[],
        help="Only find photos with this tag (may be given multiple times)",
    )
    parser.add_argument(
        "--try-prefix",
        type=str,
        help="Try adding this prefix to Immich 'original_filename' when matching photos",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="Increase output verbosity (-v for INFO, -vv for DEBUG)",
    )
    parser.add_argument("--log-file", type=str, help="Path to a log file")
    parser.add_argument(
        "--no-files",
        action="store_true",
        help="Do not read local files; instead, reset timezone offset on all matching assets to match --timezone",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files or directories to reference for date/time corrections",
    )
    return parser.parse_args(list(argv) if argv is not None else None)


def _configure_logging(args: argparse.Namespace) -> None:
    # Create a console handler and set its level
    console_handler = logging.StreamHandler()
    if args.verbose >= 2:
        console_handler.setLevel(logging.DEBUG)
    elif args.verbose == 1:
        console_handler.setLevel(logging.INFO)
    else:
        console_handler.setLevel(logging.WARNING)

    # Create a formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)

    if args.log_file:
        file_handler = logging.FileHandler(args.log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)


def _read_path(
    path: pathlib.Path, default_date: datetime, et: exiftool.helper.ExifToolHelper
) -> dict[str, datetime]:
    try:
        if path.is_dir():
            return {}
        if not path.is_file():
            raise ValueError(f"Path {path} is not a file or directory")
        if path.suffix.lower() not in {
            ".jpg",
            ".jpeg",
            ".rw2",
            ".mp4",
            ".mov",
            ".heic",
            ".tiff",
            ".avif",
            ".3gp",
            ".avi",
            ".webp",
            ".webm",
            ".m4v",
            ".m4a",
        }:
            logger.debug(f"Skipping unsupported file type: {path}")
            return {}
        metadata = et.get_tags(
            str(path), tags=["DateTimeOriginal", "SubSecTimeOriginal", "OffsetTimeOriginal"]
        )[0]
        if not metadata:
            logger.warning(f"No metadata found for {path}")
            return {}
        photo_date_str = metadata.get("EXIF:DateTimeOriginal")
        if photo_date_str is None:
            logger.info(f"No date/time metadata found for {path}")
            return {}
        if metadata.get("EXIF:OffsetTimeOriginal"):
            offset_tz = dateutil.tz.gettz("UTC" + metadata.get("EXIF:OffsetTimeOriginal"))
            default_date = default_date.astimezone(offset_tz)
        photo_date = dateutil.parser.parse(
            photo_date_str[0:8].replace(":", "-") + photo_date_str[8:],
            default=default_date,
        )
        secfrac_str = str(metadata.get("EXIF:SubSecTimeOriginal", "000"))
        while len(secfrac_str) < 6:
            secfrac_str += "0"
        photo_millis_adj = timedelta(microseconds=int(secfrac_str[0:6]))
        logger.debug(f"Read date {photo_date} (+{photo_millis_adj}) from {path}")
        return {path.stem: photo_date + photo_millis_adj}
    except TypeError as e:
        logger.error(f"Error reading metadata from {path}: {e}")
        raise


def pathfiles(*paths: str) -> Iterable[pathlib.Path]:
    """Yield all files from given paths, recursively for directories."""
    for path_str in paths:
        path = pathlib.Path(path_str)
        if path.is_file():
            yield path
        else:
            yield from filter(lambda x: x.is_file(), path.rglob("*"))


def _make_search_params(
    args: argparse.Namespace, default_tz: tzinfo | None, client: AuthenticatedClient
) -> MetadataSearchDto:
    search_params = MetadataSearchDto()
    if args.before is not None:
        before_date = dateutil.parser.parse(args.before).date()
        before_dt = datetime.combine(before_date, time(0, 0), tzinfo=default_tz)
        search_params.taken_before = before_dt
    if args.after is not None:
        after_date = dateutil.parser.parse(args.after).date()
        after_dt = datetime.combine(after_date, time(0, 0), tzinfo=default_tz)
        search_params.taken_after = after_dt + timedelta(days=1) - timedelta(milliseconds=1)
    if args.model is not None:
        search_params.model = str(args.model)
    if args.tags:
        # need to get the tags and convert to list of UUIDs
        tags_resp = get_all_tags.sync_detailed(client=client)
        if tags_resp.parsed is None:
            raise ValueError("No response from Immich server when fetching tags.")
        tag_name_to_id = {tag.name: (UUID(tag.id), tag.value) for tag in tags_resp.parsed}
        tag_value_to_id = {tag.value: UUID(tag.id) for tag in tags_resp.parsed}
        tag_ids: list[UUID] = []
        for tag in args.tags:
            if tag in tag_value_to_id:
                tag_ids.append(tag_value_to_id[tag])
            elif tag in tag_name_to_id:
                tag_id, tag_value = tag_name_to_id[tag]
                logger.warning(f"Using short name match for tag: {tag} (full name: {tag_value})")
                tag_ids.append(tag_id)
            else:
                raise ValueError(f"No such tag found on server: {tag}")
        search_params.tag_ids = tag_ids
    return search_params


def _get_asset_datetime_tz(
    client: AuthenticatedClient, asset: AssetResponseDto, orig_key: str
) -> None | tuple[None | datetime, None | tzinfo]:
    e_info = asset.exif_info
    if e_info is UNSET:
        q_resp = get_asset_info.sync_detailed(
            client=client,
            id=UUID(asset.id),
        )
        if q_resp.parsed is None:
            logger.error(f"Failed to get full info for asset ID {asset.id} ({orig_key})")
            return None
        asset = q_resp.parsed
        e_info = asset.exif_info
    assert isinstance(e_info, ExifResponseDto)
    asset_dt = None
    asset_tz = None
    if isinstance(e_info.date_time_original, datetime):
        assert isinstance(e_info.date_time_original, datetime)
        asset_tz_str = e_info.time_zone
        if asset_tz_str is None:
            asset_dt = e_info.date_time_original.replace(tzinfo=None)
        else:
            assert isinstance(asset_tz_str, str)
            asset_dt = e_info.date_time_original
            asset_tz = dateutil.tz.gettz(asset_tz_str)
            if asset_tz is None:
                logger.warning(
                    f"Asset ID {asset.id} ({orig_key}) has unknown time zone: {e_info.time_zone}"
                )
            else:
                asset_dt = asset_dt.astimezone(asset_tz)
    return asset_dt, asset_tz


def _get_all_assets(
    client: AuthenticatedClient, search_params: MetadataSearchDto
) -> Iterable[AssetResponseDto]:
    keep_going = True
    while keep_going:
        keep_going = False
        response = search_assets.sync_detailed(client=client, body=search_params)
        if response.parsed is None:
            raise ImmichClientError("No response from Immich server to asset search.")
        assets = response.parsed.assets
        logger.debug(
            f"Found {assets.count} assets matching search criteria. (next page: {assets.next_page})"
        )
        yield from assets.items
        if assets.next_page is not None:
            keep_going = True
            search_params.page = int(assets.next_page)


def run(argv: None | Iterable[str] = None) -> int:
    """
    immich-fixer CLI entrypoint function.

    Args:
        argv: Optional iterable of argument strings (defaults to sys.argv[1:]).

    Returns:
        Exit code (0 on success).
    """
    args = _parse_args(argv)

    if not args.paths and not args.no_files:
        # If no paths provided, show help and exit with non-zero code to indicate nothing done.
        print("No paths provided.\n")
        _parse_args(["-h"])
        return 1
    if args.paths and args.no_files:
        print("Paths provided but --no-files specified.\n")
        _parse_args(["-h"])
        return 1

    _configure_logging(args)
    if args.timezone is None:
        default_tz = None
    else:
        default_tz = dateutil.tz.gettz(args.timezone)
        if default_tz is None:
            print(f"No such time zone known: {args.timezone!r}")
            return 1
    default_date = datetime.now(tz=default_tz).replace(second=0, microsecond=0)
    logger.debug(f"Basing times on default date {default_date.isoformat()}, timezone {default_tz}")

    wisdom: dict[str, datetime] = {}
    if not args.no_files:
        processed = 0
        with exiftool.ExifToolHelper() as et_helper:
            for path in pathfiles(*args.paths):
                rv = _read_path(path=path, default_date=default_date, et=et_helper)
                if rv:
                    wisdom.update(rv)
                    processed += 1

        if processed == 0:
            logger.warning("No valid files processed; nothing to do.")
            return 1
        logger.info(f"Processed {processed} path(s).")

    with AuthenticatedClient.from_api_key(base_url=args.url, api_key=args.api_key) as client:
        try:
            search_params = _make_search_params(args, default_tz, client)
        except ValueError as e:
            logger.error(e.args[0])
            return 1
        for asset in _get_all_assets(client, search_params):
            orig_key = pathlib.Path(asset.original_file_name).stem
            if (
                not args.no_files
                and args.try_prefix is not None
                and orig_key not in wisdom
                and (args.try_prefix + orig_key) in wisdom
            ):
                logger.debug(
                    f"Trying prefix {args.try_prefix!r} for asset ID {asset.id} ({orig_key})"
                )
                orig_key = args.try_prefix + orig_key
            if args.no_files or orig_key in wisdom:
                asset_time_info = _get_asset_datetime_tz(client, asset, orig_key)
                if asset_time_info is None:
                    logger.debug(f"Skipping asset ID {asset.id} ({orig_key}) due to client error")
                    continue
                asset_dt, asset_tz = asset_time_info
                correct_date: None | datetime
                if args.no_files:
                    if default_tz is not None and asset_dt is not None:
                        correct_date = asset_dt.replace(tzinfo=default_tz)
                    else:
                        correct_date = asset_dt
                else:
                    correct_date = wisdom[orig_key]
                if correct_date is None:
                    logger.debug(
                        f"Cannot determine correct date for asset ID {asset.id} ({orig_key}); skipping"
                    )
                    continue
                if correct_date.tzinfo is None and asset_tz is not None:
                    correct_date = correct_date.replace(tzinfo=asset_tz)
                if asset_dt == correct_date:
                    if correct_date.tzinfo == asset_tz or (
                        correct_date.tzinfo is not None
                        and asset_tz is not None
                        and asset_tz.utcoffset(correct_date)
                        == correct_date.tzinfo.utcoffset(correct_date)
                    ):
                        logger.debug(
                            f"Asset ID {asset.id} ({orig_key}) already has correct date {correct_date.isoformat()}"
                        )
                        continue
                if args.dry_run:
                    print(
                        f"Would update asset ID {asset.id} ({orig_key}) to date {correct_date.isoformat()}"
                        f" from {'None' if asset_dt is None else asset_dt.isoformat()}"
                    )
                else:
                    logger.info(
                        f"Updating asset ID {asset.id} ({orig_key}) to date {correct_date.isoformat()}"
                        f" from {'None' if asset_dt is None else asset_dt.isoformat()}"
                    )
                    update_asset.sync(
                        client=client,
                        id=UUID(asset.id),
                        body=UpdateAssetDto(date_time_original=correct_date.isoformat()),
                    )
            else:
                logger.debug(
                    f"No matching local file found for asset ID {asset.id} ({asset.original_file_name})"
                )
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1:]))
