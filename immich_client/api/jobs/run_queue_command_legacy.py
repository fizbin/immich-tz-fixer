from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.queue_command_dto import QueueCommandDto
from ...models.queue_name import QueueName
from ...models.queue_response_dto import QueueResponseDto
from ...types import Response


def _get_kwargs(
    name: QueueName,
    *,
    body: QueueCommandDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/jobs/{name}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> QueueResponseDto | None:
    if response.status_code == 200:
        response_200 = QueueResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[QueueResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: QueueName,
    *,
    client: AuthenticatedClient,
    body: QueueCommandDto,
) -> Response[QueueResponseDto]:
    """Run jobs

     Queue all assets for a specific job type. Defaults to only queueing assets that have not yet been
    processed, but the force command can be used to re-process all assets.

    Args:
        name (QueueName):
        body (QueueCommandDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueueResponseDto]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: QueueName,
    *,
    client: AuthenticatedClient,
    body: QueueCommandDto,
) -> QueueResponseDto | None:
    """Run jobs

     Queue all assets for a specific job type. Defaults to only queueing assets that have not yet been
    processed, but the force command can be used to re-process all assets.

    Args:
        name (QueueName):
        body (QueueCommandDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueueResponseDto
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: QueueName,
    *,
    client: AuthenticatedClient,
    body: QueueCommandDto,
) -> Response[QueueResponseDto]:
    """Run jobs

     Queue all assets for a specific job type. Defaults to only queueing assets that have not yet been
    processed, but the force command can be used to re-process all assets.

    Args:
        name (QueueName):
        body (QueueCommandDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueueResponseDto]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: QueueName,
    *,
    client: AuthenticatedClient,
    body: QueueCommandDto,
) -> QueueResponseDto | None:
    """Run jobs

     Queue all assets for a specific job type. Defaults to only queueing assets that have not yet been
    processed, but the force command can be used to re-process all assets.

    Args:
        name (QueueName):
        body (QueueCommandDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueueResponseDto
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
