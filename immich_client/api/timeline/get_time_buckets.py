from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_order import AssetOrder
from ...models.asset_visibility import AssetVisibility
from ...models.time_buckets_response_dto import TimeBucketsResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    album_id: UUID | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    order: AssetOrder | Unset = UNSET,
    person_id: UUID | Unset = UNSET,
    slug: str | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    visibility: AssetVisibility | Unset = UNSET,
    with_coordinates: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_stacked: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_album_id: str | Unset = UNSET
    if not isinstance(album_id, Unset):
        json_album_id = str(album_id)
    params["albumId"] = json_album_id

    params["isFavorite"] = is_favorite

    params["isTrashed"] = is_trashed

    params["key"] = key

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_person_id: str | Unset = UNSET
    if not isinstance(person_id, Unset):
        json_person_id = str(person_id)
    params["personId"] = json_person_id

    params["slug"] = slug

    json_tag_id: str | Unset = UNSET
    if not isinstance(tag_id, Unset):
        json_tag_id = str(tag_id)
    params["tagId"] = json_tag_id

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    json_visibility: str | Unset = UNSET
    if not isinstance(visibility, Unset):
        json_visibility = visibility.value

    params["visibility"] = json_visibility

    params["withCoordinates"] = with_coordinates

    params["withPartners"] = with_partners

    params["withStacked"] = with_stacked

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeline/buckets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[TimeBucketsResponseDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TimeBucketsResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[TimeBucketsResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    album_id: UUID | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    order: AssetOrder | Unset = UNSET,
    person_id: UUID | Unset = UNSET,
    slug: str | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    visibility: AssetVisibility | Unset = UNSET,
    with_coordinates: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_stacked: bool | Unset = UNSET,
) -> Response[list[TimeBucketsResponseDto]]:
    """Get time buckets

     Retrieve a list of all minimal time buckets.

    Args:
        album_id (UUID | Unset):
        is_favorite (bool | Unset):
        is_trashed (bool | Unset):
        key (str | Unset):
        order (AssetOrder | Unset):
        person_id (UUID | Unset):
        slug (str | Unset):
        tag_id (UUID | Unset):
        user_id (UUID | Unset):
        visibility (AssetVisibility | Unset):
        with_coordinates (bool | Unset):
        with_partners (bool | Unset):
        with_stacked (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TimeBucketsResponseDto]]
    """

    kwargs = _get_kwargs(
        album_id=album_id,
        is_favorite=is_favorite,
        is_trashed=is_trashed,
        key=key,
        order=order,
        person_id=person_id,
        slug=slug,
        tag_id=tag_id,
        user_id=user_id,
        visibility=visibility,
        with_coordinates=with_coordinates,
        with_partners=with_partners,
        with_stacked=with_stacked,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    album_id: UUID | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    order: AssetOrder | Unset = UNSET,
    person_id: UUID | Unset = UNSET,
    slug: str | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    visibility: AssetVisibility | Unset = UNSET,
    with_coordinates: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_stacked: bool | Unset = UNSET,
) -> list[TimeBucketsResponseDto] | None:
    """Get time buckets

     Retrieve a list of all minimal time buckets.

    Args:
        album_id (UUID | Unset):
        is_favorite (bool | Unset):
        is_trashed (bool | Unset):
        key (str | Unset):
        order (AssetOrder | Unset):
        person_id (UUID | Unset):
        slug (str | Unset):
        tag_id (UUID | Unset):
        user_id (UUID | Unset):
        visibility (AssetVisibility | Unset):
        with_coordinates (bool | Unset):
        with_partners (bool | Unset):
        with_stacked (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TimeBucketsResponseDto]
    """

    return sync_detailed(
        client=client,
        album_id=album_id,
        is_favorite=is_favorite,
        is_trashed=is_trashed,
        key=key,
        order=order,
        person_id=person_id,
        slug=slug,
        tag_id=tag_id,
        user_id=user_id,
        visibility=visibility,
        with_coordinates=with_coordinates,
        with_partners=with_partners,
        with_stacked=with_stacked,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    album_id: UUID | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    order: AssetOrder | Unset = UNSET,
    person_id: UUID | Unset = UNSET,
    slug: str | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    visibility: AssetVisibility | Unset = UNSET,
    with_coordinates: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_stacked: bool | Unset = UNSET,
) -> Response[list[TimeBucketsResponseDto]]:
    """Get time buckets

     Retrieve a list of all minimal time buckets.

    Args:
        album_id (UUID | Unset):
        is_favorite (bool | Unset):
        is_trashed (bool | Unset):
        key (str | Unset):
        order (AssetOrder | Unset):
        person_id (UUID | Unset):
        slug (str | Unset):
        tag_id (UUID | Unset):
        user_id (UUID | Unset):
        visibility (AssetVisibility | Unset):
        with_coordinates (bool | Unset):
        with_partners (bool | Unset):
        with_stacked (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TimeBucketsResponseDto]]
    """

    kwargs = _get_kwargs(
        album_id=album_id,
        is_favorite=is_favorite,
        is_trashed=is_trashed,
        key=key,
        order=order,
        person_id=person_id,
        slug=slug,
        tag_id=tag_id,
        user_id=user_id,
        visibility=visibility,
        with_coordinates=with_coordinates,
        with_partners=with_partners,
        with_stacked=with_stacked,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    album_id: UUID | Unset = UNSET,
    is_favorite: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    order: AssetOrder | Unset = UNSET,
    person_id: UUID | Unset = UNSET,
    slug: str | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    visibility: AssetVisibility | Unset = UNSET,
    with_coordinates: bool | Unset = UNSET,
    with_partners: bool | Unset = UNSET,
    with_stacked: bool | Unset = UNSET,
) -> list[TimeBucketsResponseDto] | None:
    """Get time buckets

     Retrieve a list of all minimal time buckets.

    Args:
        album_id (UUID | Unset):
        is_favorite (bool | Unset):
        is_trashed (bool | Unset):
        key (str | Unset):
        order (AssetOrder | Unset):
        person_id (UUID | Unset):
        slug (str | Unset):
        tag_id (UUID | Unset):
        user_id (UUID | Unset):
        visibility (AssetVisibility | Unset):
        with_coordinates (bool | Unset):
        with_partners (bool | Unset):
        with_stacked (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TimeBucketsResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            album_id=album_id,
            is_favorite=is_favorite,
            is_trashed=is_trashed,
            key=key,
            order=order,
            person_id=person_id,
            slug=slug,
            tag_id=tag_id,
            user_id=user_id,
            visibility=visibility,
            with_coordinates=with_coordinates,
            with_partners=with_partners,
            with_stacked=with_stacked,
        )
    ).parsed
