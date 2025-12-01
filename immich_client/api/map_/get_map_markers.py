import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.map_marker_response_dto import MapMarkerResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    file_created_after: datetime.datetime | Unset = UNSET,
    file_created_before: datetime.datetime | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_shared_albums: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_file_created_after: str | Unset = UNSET
    if not isinstance(file_created_after, Unset):
        json_file_created_after = file_created_after.isoformat()
    params["fileCreatedAfter"] = json_file_created_after

    json_file_created_before: str | Unset = UNSET
    if not isinstance(file_created_before, Unset):
        json_file_created_before = file_created_before.isoformat()
    params["fileCreatedBefore"] = json_file_created_before

    params["isArchived"] = is_archived

    params["isFavorite"] = is_favorite

    params["withPartners"] = with_partners

    params["withSharedAlbums"] = with_shared_albums

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/map/markers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[MapMarkerResponseDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MapMarkerResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[MapMarkerResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    file_created_after: datetime.datetime | Unset = UNSET,
    file_created_before: datetime.datetime | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_shared_albums: bool | Unset = UNSET,
) -> Response[list[MapMarkerResponseDto]]:
    """Retrieve map markers

     Retrieve a list of latitude and longitude coordinates for every asset with location data.

    Args:
        file_created_after (datetime.datetime | Unset):
        file_created_before (datetime.datetime | Unset):
        is_archived (bool | Unset):
        is_favorite (bool | Unset):
        with_partners (bool | Unset):
        with_shared_albums (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[MapMarkerResponseDto]]
    """

    kwargs = _get_kwargs(
        file_created_after=file_created_after,
        file_created_before=file_created_before,
        is_archived=is_archived,
        is_favorite=is_favorite,
        with_partners=with_partners,
        with_shared_albums=with_shared_albums,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    file_created_after: datetime.datetime | Unset = UNSET,
    file_created_before: datetime.datetime | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_shared_albums: bool | Unset = UNSET,
) -> list[MapMarkerResponseDto] | None:
    """Retrieve map markers

     Retrieve a list of latitude and longitude coordinates for every asset with location data.

    Args:
        file_created_after (datetime.datetime | Unset):
        file_created_before (datetime.datetime | Unset):
        is_archived (bool | Unset):
        is_favorite (bool | Unset):
        with_partners (bool | Unset):
        with_shared_albums (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[MapMarkerResponseDto]
    """

    return sync_detailed(
        client=client,
        file_created_after=file_created_after,
        file_created_before=file_created_before,
        is_archived=is_archived,
        is_favorite=is_favorite,
        with_partners=with_partners,
        with_shared_albums=with_shared_albums,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    file_created_after: datetime.datetime | Unset = UNSET,
    file_created_before: datetime.datetime | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_shared_albums: bool | Unset = UNSET,
) -> Response[list[MapMarkerResponseDto]]:
    """Retrieve map markers

     Retrieve a list of latitude and longitude coordinates for every asset with location data.

    Args:
        file_created_after (datetime.datetime | Unset):
        file_created_before (datetime.datetime | Unset):
        is_archived (bool | Unset):
        is_favorite (bool | Unset):
        with_partners (bool | Unset):
        with_shared_albums (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[MapMarkerResponseDto]]
    """

    kwargs = _get_kwargs(
        file_created_after=file_created_after,
        file_created_before=file_created_before,
        is_archived=is_archived,
        is_favorite=is_favorite,
        with_partners=with_partners,
        with_shared_albums=with_shared_albums,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    file_created_after: datetime.datetime | Unset = UNSET,
    file_created_before: datetime.datetime | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_shared_albums: bool | Unset = UNSET,
) -> list[MapMarkerResponseDto] | None:
    """Retrieve map markers

     Retrieve a list of latitude and longitude coordinates for every asset with location data.

    Args:
        file_created_after (datetime.datetime | Unset):
        file_created_before (datetime.datetime | Unset):
        is_archived (bool | Unset):
        is_favorite (bool | Unset):
        with_partners (bool | Unset):
        with_shared_albums (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[MapMarkerResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            file_created_after=file_created_after,
            file_created_before=file_created_before,
            is_archived=is_archived,
            is_favorite=is_favorite,
            with_partners=with_partners,
            with_shared_albums=with_shared_albums,
        )
    ).parsed
