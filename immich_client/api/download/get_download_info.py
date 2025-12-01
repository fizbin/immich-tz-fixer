from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_info_dto import DownloadInfoDto
from ...models.download_response_dto import DownloadResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DownloadInfoDto,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["key"] = key

    params["slug"] = slug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/download/info",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DownloadResponseDto | None:
    if response.status_code == 201:
        response_201 = DownloadResponseDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DownloadResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DownloadInfoDto,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> Response[DownloadResponseDto]:
    """Retrieve download information

     Retrieve information about how to request a download for the specified assets or album. The response
    includes groups of assets that can be downloaded together.

    Args:
        key (str | Unset):
        slug (str | Unset):
        body (DownloadInfoDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
        key=key,
        slug=slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DownloadInfoDto,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> DownloadResponseDto | None:
    """Retrieve download information

     Retrieve information about how to request a download for the specified assets or album. The response
    includes groups of assets that can be downloaded together.

    Args:
        key (str | Unset):
        slug (str | Unset):
        body (DownloadInfoDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadResponseDto
    """

    return sync_detailed(
        client=client,
        body=body,
        key=key,
        slug=slug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DownloadInfoDto,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> Response[DownloadResponseDto]:
    """Retrieve download information

     Retrieve information about how to request a download for the specified assets or album. The response
    includes groups of assets that can be downloaded together.

    Args:
        key (str | Unset):
        slug (str | Unset):
        body (DownloadInfoDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
        key=key,
        slug=slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DownloadInfoDto,
    key: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> DownloadResponseDto | None:
    """Retrieve download information

     Retrieve information about how to request a download for the specified assets or album. The response
    includes groups of assets that can be downloaded together.

    Args:
        key (str | Unset):
        slug (str | Unset):
        body (DownloadInfoDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            key=key,
            slug=slug,
        )
    ).parsed
