from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_response_dto import AlbumResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_id: UUID | Unset = UNSET,
    shared: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_asset_id: str | Unset = UNSET
    if not isinstance(asset_id, Unset):
        json_asset_id = str(asset_id)
    params["assetId"] = json_asset_id

    params["shared"] = shared

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/albums",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[AlbumResponseDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AlbumResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[AlbumResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_id: UUID | Unset = UNSET,
    shared: bool | Unset = UNSET,
) -> Response[list[AlbumResponseDto]]:
    """List all albums

     Retrieve a list of albums available to the authenticated user.

    Args:
        asset_id (UUID | Unset):
        shared (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AlbumResponseDto]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        shared=shared,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset_id: UUID | Unset = UNSET,
    shared: bool | Unset = UNSET,
) -> list[AlbumResponseDto] | None:
    """List all albums

     Retrieve a list of albums available to the authenticated user.

    Args:
        asset_id (UUID | Unset):
        shared (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AlbumResponseDto]
    """

    return sync_detailed(
        client=client,
        asset_id=asset_id,
        shared=shared,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_id: UUID | Unset = UNSET,
    shared: bool | Unset = UNSET,
) -> Response[list[AlbumResponseDto]]:
    """List all albums

     Retrieve a list of albums available to the authenticated user.

    Args:
        asset_id (UUID | Unset):
        shared (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AlbumResponseDto]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        shared=shared,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_id: UUID | Unset = UNSET,
    shared: bool | Unset = UNSET,
) -> list[AlbumResponseDto] | None:
    """List all albums

     Retrieve a list of albums available to the authenticated user.

    Args:
        asset_id (UUID | Unset):
        shared (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AlbumResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_id=asset_id,
            shared=shared,
        )
    ).parsed
