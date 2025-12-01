from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.shared_link_response_dto import SharedLinkResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    key: str | Unset = UNSET,
    password: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    token: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["key"] = key

    params["password"] = password

    params["slug"] = slug

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/shared-links/me",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SharedLinkResponseDto | None:
    if response.status_code == 200:
        response_200 = SharedLinkResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SharedLinkResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    password: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    token: str | Unset = UNSET,
) -> Response[SharedLinkResponseDto]:
    """Retrieve current shared link

     Retrieve the current shared link associated with authentication method.

    Args:
        key (str | Unset):
        password (str | Unset):  Example: password.
        slug (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SharedLinkResponseDto]
    """

    kwargs = _get_kwargs(
        key=key,
        password=password,
        slug=slug,
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    password: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    token: str | Unset = UNSET,
) -> SharedLinkResponseDto | None:
    """Retrieve current shared link

     Retrieve the current shared link associated with authentication method.

    Args:
        key (str | Unset):
        password (str | Unset):  Example: password.
        slug (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SharedLinkResponseDto
    """

    return sync_detailed(
        client=client,
        key=key,
        password=password,
        slug=slug,
        token=token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    password: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    token: str | Unset = UNSET,
) -> Response[SharedLinkResponseDto]:
    """Retrieve current shared link

     Retrieve the current shared link associated with authentication method.

    Args:
        key (str | Unset):
        password (str | Unset):  Example: password.
        slug (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SharedLinkResponseDto]
    """

    kwargs = _get_kwargs(
        key=key,
        password=password,
        slug=slug,
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    password: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    token: str | Unset = UNSET,
) -> SharedLinkResponseDto | None:
    """Retrieve current shared link

     Retrieve the current shared link associated with authentication method.

    Args:
        key (str | Unset):
        password (str | Unset):  Example: password.
        slug (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SharedLinkResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            key=key,
            password=password,
            slug=slug,
            token=token,
        )
    ).parsed
