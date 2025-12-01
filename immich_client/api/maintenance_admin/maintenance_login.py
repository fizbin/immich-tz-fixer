from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.maintenance_auth_dto import MaintenanceAuthDto
from ...models.maintenance_login_dto import MaintenanceLoginDto
from ...types import Response


def _get_kwargs(
    *,
    body: MaintenanceLoginDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/admin/maintenance/login",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MaintenanceAuthDto | None:
    if response.status_code == 201:
        response_201 = MaintenanceAuthDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MaintenanceAuthDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MaintenanceLoginDto,
) -> Response[MaintenanceAuthDto]:
    """Log into maintenance mode

     Login with maintenance token or cookie to receive current information and perform further actions.

    Args:
        body (MaintenanceLoginDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceAuthDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: MaintenanceLoginDto,
) -> MaintenanceAuthDto | None:
    """Log into maintenance mode

     Login with maintenance token or cookie to receive current information and perform further actions.

    Args:
        body (MaintenanceLoginDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceAuthDto
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MaintenanceLoginDto,
) -> Response[MaintenanceAuthDto]:
    """Log into maintenance mode

     Login with maintenance token or cookie to receive current information and perform further actions.

    Args:
        body (MaintenanceLoginDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceAuthDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MaintenanceLoginDto,
) -> MaintenanceAuthDto | None:
    """Log into maintenance mode

     Login with maintenance token or cookie to receive current information and perform further actions.

    Args:
        body (MaintenanceLoginDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceAuthDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
