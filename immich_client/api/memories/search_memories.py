import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.memory_response_dto import MemoryResponseDto
from ...models.memory_search_order import MemorySearchOrder
from ...models.memory_type import MemoryType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    for_: datetime.datetime | Unset = UNSET,
    is_saved: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    order: MemorySearchOrder | Unset = UNSET,
    size: int | Unset = UNSET,
    type_: MemoryType | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_for_: str | Unset = UNSET
    if not isinstance(for_, Unset):
        json_for_ = for_.isoformat()
    params["for"] = json_for_

    params["isSaved"] = is_saved

    params["isTrashed"] = is_trashed

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["size"] = size

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/memories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[MemoryResponseDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MemoryResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[MemoryResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    for_: datetime.datetime | Unset = UNSET,
    is_saved: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    order: MemorySearchOrder | Unset = UNSET,
    size: int | Unset = UNSET,
    type_: MemoryType | Unset = UNSET,
) -> Response[list[MemoryResponseDto]]:
    """Retrieve memories

     Retrieve a list of memories. Memories are sorted descending by creation date by default, although
    they can also be sorted in ascending order, or randomly.

    Args:
        for_ (datetime.datetime | Unset):
        is_saved (bool | Unset):
        is_trashed (bool | Unset):
        order (MemorySearchOrder | Unset):
        size (int | Unset):
        type_ (MemoryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[MemoryResponseDto]]
    """

    kwargs = _get_kwargs(
        for_=for_,
        is_saved=is_saved,
        is_trashed=is_trashed,
        order=order,
        size=size,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    for_: datetime.datetime | Unset = UNSET,
    is_saved: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    order: MemorySearchOrder | Unset = UNSET,
    size: int | Unset = UNSET,
    type_: MemoryType | Unset = UNSET,
) -> list[MemoryResponseDto] | None:
    """Retrieve memories

     Retrieve a list of memories. Memories are sorted descending by creation date by default, although
    they can also be sorted in ascending order, or randomly.

    Args:
        for_ (datetime.datetime | Unset):
        is_saved (bool | Unset):
        is_trashed (bool | Unset):
        order (MemorySearchOrder | Unset):
        size (int | Unset):
        type_ (MemoryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[MemoryResponseDto]
    """

    return sync_detailed(
        client=client,
        for_=for_,
        is_saved=is_saved,
        is_trashed=is_trashed,
        order=order,
        size=size,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    for_: datetime.datetime | Unset = UNSET,
    is_saved: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    order: MemorySearchOrder | Unset = UNSET,
    size: int | Unset = UNSET,
    type_: MemoryType | Unset = UNSET,
) -> Response[list[MemoryResponseDto]]:
    """Retrieve memories

     Retrieve a list of memories. Memories are sorted descending by creation date by default, although
    they can also be sorted in ascending order, or randomly.

    Args:
        for_ (datetime.datetime | Unset):
        is_saved (bool | Unset):
        is_trashed (bool | Unset):
        order (MemorySearchOrder | Unset):
        size (int | Unset):
        type_ (MemoryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[MemoryResponseDto]]
    """

    kwargs = _get_kwargs(
        for_=for_,
        is_saved=is_saved,
        is_trashed=is_trashed,
        order=order,
        size=size,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    for_: datetime.datetime | Unset = UNSET,
    is_saved: bool | Unset = UNSET,
    is_trashed: bool | Unset = UNSET,
    order: MemorySearchOrder | Unset = UNSET,
    size: int | Unset = UNSET,
    type_: MemoryType | Unset = UNSET,
) -> list[MemoryResponseDto] | None:
    """Retrieve memories

     Retrieve a list of memories. Memories are sorted descending by creation date by default, although
    they can also be sorted in ascending order, or randomly.

    Args:
        for_ (datetime.datetime | Unset):
        is_saved (bool | Unset):
        is_trashed (bool | Unset):
        order (MemorySearchOrder | Unset):
        size (int | Unset):
        type_ (MemoryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[MemoryResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            for_=for_,
            is_saved=is_saved,
            is_trashed=is_trashed,
            order=order,
            size=size,
            type_=type_,
        )
    ).parsed
