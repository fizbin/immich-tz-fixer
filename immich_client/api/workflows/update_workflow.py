from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workflow_response_dto import WorkflowResponseDto
from ...models.workflow_update_dto import WorkflowUpdateDto
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: WorkflowUpdateDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/workflows/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WorkflowResponseDto | None:
    if response.status_code == 200:
        response_200 = WorkflowResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WorkflowResponseDto]:
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
    body: WorkflowUpdateDto,
) -> Response[WorkflowResponseDto]:
    """Update a workflow

     Update the information of a specific workflow by its ID. This endpoint can be used to update the
    workflow name, description, trigger type, filters and actions order, etc.

    Args:
        id (UUID):
        body (WorkflowUpdateDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowResponseDto]
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
    body: WorkflowUpdateDto,
) -> WorkflowResponseDto | None:
    """Update a workflow

     Update the information of a specific workflow by its ID. This endpoint can be used to update the
    workflow name, description, trigger type, filters and actions order, etc.

    Args:
        id (UUID):
        body (WorkflowUpdateDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowResponseDto
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
    body: WorkflowUpdateDto,
) -> Response[WorkflowResponseDto]:
    """Update a workflow

     Update the information of a specific workflow by its ID. This endpoint can be used to update the
    workflow name, description, trigger type, filters and actions order, etc.

    Args:
        id (UUID):
        body (WorkflowUpdateDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowResponseDto]
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
    body: WorkflowUpdateDto,
) -> WorkflowResponseDto | None:
    """Update a workflow

     Update the information of a specific workflow by its ID. This endpoint can be used to update the
    workflow name, description, trigger type, filters and actions order, etc.

    Args:
        id (UUID):
        body (WorkflowUpdateDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowResponseDto
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
