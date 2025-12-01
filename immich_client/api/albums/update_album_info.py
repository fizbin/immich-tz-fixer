from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_response_dto import AlbumResponseDto
from ...models.update_album_dto import UpdateAlbumDto
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: UpdateAlbumDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/albums/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: UpdateAlbumDto,
) -> Response[AlbumResponseDto]:
    """Update an album

     Update the information of a specific album by its ID. This endpoint can be used to update the album
    name, description, sort order, etc. However, it is not used to add or remove assets or users from
    the album.

    Args:
        id (UUID):
        body (UpdateAlbumDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateAlbumDto,
) -> AlbumResponseDto | None:
    """Update an album

     Update the information of a specific album by its ID. This endpoint can be used to update the album
    name, description, sort order, etc. However, it is not used to add or remove assets or users from
    the album.

    Args:
        id (UUID):
        body (UpdateAlbumDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumResponseDto
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateAlbumDto,
) -> Response[AlbumResponseDto]:
    """Update an album

     Update the information of a specific album by its ID. This endpoint can be used to update the album
    name, description, sort order, etc. However, it is not used to add or remove assets or users from
    the album.

    Args:
        id (UUID):
        body (UpdateAlbumDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateAlbumDto,
) -> AlbumResponseDto | None:
    """Update an album

     Update the information of a specific album by its ID. This endpoint can be used to update the album
    name, description, sort order, etc. However, it is not used to add or remove assets or users from
    the album.

    Args:
        id (UUID):
        body (UpdateAlbumDto):

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
            body=body,
        )
    ).parsed
