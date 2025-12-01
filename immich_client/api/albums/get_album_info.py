from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_response_dto import AlbumResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    without_assets: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["key"] = key

    params["slug"] = slug

    params["withoutAssets"] = without_assets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/albums/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumResponseDto | None:
    if response.status_code == 200:
        response_200 = AlbumResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlbumResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    without_assets: bool | Unset = UNSET,
) -> Response[AlbumResponseDto]:
    """Retrieve an album

     Retrieve information about a specific album by its ID.

    Args:
        id (UUID):
        key (str | Unset):
        slug (str | Unset):
        without_assets (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        key=key,
        slug=slug,
        without_assets=without_assets,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    without_assets: bool | Unset = UNSET,
) -> AlbumResponseDto | None:
    """Retrieve an album

     Retrieve information about a specific album by its ID.

    Args:
        id (UUID):
        key (str | Unset):
        slug (str | Unset):
        without_assets (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumResponseDto
    """

    return sync_detailed(
        id=id,
        client=client,
        key=key,
        slug=slug,
        without_assets=without_assets,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    without_assets: bool | Unset = UNSET,
) -> Response[AlbumResponseDto]:
    """Retrieve an album

     Retrieve information about a specific album by its ID.

    Args:
        id (UUID):
        key (str | Unset):
        slug (str | Unset):
        without_assets (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        key=key,
        slug=slug,
        without_assets=without_assets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    without_assets: bool | Unset = UNSET,
) -> AlbumResponseDto | None:
    """Retrieve an album

     Retrieve information about a specific album by its ID.

    Args:
        id (UUID):
        key (str | Unset):
        slug (str | Unset):
        without_assets (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumResponseDto
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            key=key,
            slug=slug,
            without_assets=without_assets,
        )
    ).parsed
