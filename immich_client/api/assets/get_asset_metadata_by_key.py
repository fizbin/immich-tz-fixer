from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_metadata_key import AssetMetadataKey
from ...models.asset_metadata_response_dto import AssetMetadataResponseDto
from ...types import Response


def _get_kwargs(
    id: UUID,
    key: AssetMetadataKey,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/assets/{id}/metadata/{key}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetMetadataResponseDto | None:
    if response.status_code == 200:
        response_200 = AssetMetadataResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AssetMetadataResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    key: AssetMetadataKey,
    *,
    client: AuthenticatedClient,
) -> Response[AssetMetadataResponseDto]:
    """Retrieve asset metadata by key

     Retrieve the value of a specific metadata key associated with the specified asset.

    Args:
        id (UUID):
        key (AssetMetadataKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetMetadataResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    key: AssetMetadataKey,
    *,
    client: AuthenticatedClient,
) -> AssetMetadataResponseDto | None:
    """Retrieve asset metadata by key

     Retrieve the value of a specific metadata key associated with the specified asset.

    Args:
        id (UUID):
        key (AssetMetadataKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetMetadataResponseDto
    """

    return sync_detailed(
        id=id,
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    key: AssetMetadataKey,
    *,
    client: AuthenticatedClient,
) -> Response[AssetMetadataResponseDto]:
    """Retrieve asset metadata by key

     Retrieve the value of a specific metadata key associated with the specified asset.

    Args:
        id (UUID):
        key (AssetMetadataKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetMetadataResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    key: AssetMetadataKey,
    *,
    client: AuthenticatedClient,
) -> AssetMetadataResponseDto | None:
    """Retrieve asset metadata by key

     Retrieve the value of a specific metadata key associated with the specified asset.

    Args:
        id (UUID):
        key (AssetMetadataKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetMetadataResponseDto
    """

    return (
        await asyncio_detailed(
            id=id,
            key=key,
            client=client,
        )
    ).parsed
