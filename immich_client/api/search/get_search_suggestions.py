from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_suggestion_type import SearchSuggestionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    country: str | Unset = UNSET,
    include_null: bool | Unset = UNSET,
    lens_model: str | Unset = UNSET,
    make: str | Unset = UNSET,
    model: str | Unset = UNSET,
    state: str | Unset = UNSET,
    type_: SearchSuggestionType,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["country"] = country

    params["includeNull"] = include_null

    params["lensModel"] = lens_model

    params["make"] = make

    params["model"] = model

    params["state"] = state

    json_type_ = type_.value
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search/suggestions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[str] | None:
    if response.status_code == 200:
        response_200 = cast(list[str], response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    country: str | Unset = UNSET,
    include_null: bool | Unset = UNSET,
    lens_model: str | Unset = UNSET,
    make: str | Unset = UNSET,
    model: str | Unset = UNSET,
    state: str | Unset = UNSET,
    type_: SearchSuggestionType,
) -> Response[list[str]]:
    """Retrieve search suggestions

     Retrieve search suggestions based on partial input. This endpoint is used for typeahead search
    features.

    Args:
        country (str | Unset):
        include_null (bool | Unset):
        lens_model (str | Unset):
        make (str | Unset):
        model (str | Unset):
        state (str | Unset):
        type_ (SearchSuggestionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[str]]
    """

    kwargs = _get_kwargs(
        country=country,
        include_null=include_null,
        lens_model=lens_model,
        make=make,
        model=model,
        state=state,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    country: str | Unset = UNSET,
    include_null: bool | Unset = UNSET,
    lens_model: str | Unset = UNSET,
    make: str | Unset = UNSET,
    model: str | Unset = UNSET,
    state: str | Unset = UNSET,
    type_: SearchSuggestionType,
) -> list[str] | None:
    """Retrieve search suggestions

     Retrieve search suggestions based on partial input. This endpoint is used for typeahead search
    features.

    Args:
        country (str | Unset):
        include_null (bool | Unset):
        lens_model (str | Unset):
        make (str | Unset):
        model (str | Unset):
        state (str | Unset):
        type_ (SearchSuggestionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[str]
    """

    return sync_detailed(
        client=client,
        country=country,
        include_null=include_null,
        lens_model=lens_model,
        make=make,
        model=model,
        state=state,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    country: str | Unset = UNSET,
    include_null: bool | Unset = UNSET,
    lens_model: str | Unset = UNSET,
    make: str | Unset = UNSET,
    model: str | Unset = UNSET,
    state: str | Unset = UNSET,
    type_: SearchSuggestionType,
) -> Response[list[str]]:
    """Retrieve search suggestions

     Retrieve search suggestions based on partial input. This endpoint is used for typeahead search
    features.

    Args:
        country (str | Unset):
        include_null (bool | Unset):
        lens_model (str | Unset):
        make (str | Unset):
        model (str | Unset):
        state (str | Unset):
        type_ (SearchSuggestionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[str]]
    """

    kwargs = _get_kwargs(
        country=country,
        include_null=include_null,
        lens_model=lens_model,
        make=make,
        model=model,
        state=state,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    country: str | Unset = UNSET,
    include_null: bool | Unset = UNSET,
    lens_model: str | Unset = UNSET,
    make: str | Unset = UNSET,
    model: str | Unset = UNSET,
    state: str | Unset = UNSET,
    type_: SearchSuggestionType,
) -> list[str] | None:
    """Retrieve search suggestions

     Retrieve search suggestions based on partial input. This endpoint is used for typeahead search
    features.

    Args:
        country (str | Unset):
        include_null (bool | Unset):
        lens_model (str | Unset):
        make (str | Unset):
        model (str | Unset):
        state (str | Unset):
        type_ (SearchSuggestionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[str]
    """

    return (
        await asyncio_detailed(
            client=client,
            country=country,
            include_null=include_null,
            lens_model=lens_model,
            make=make,
            model=model,
            state=state,
            type_=type_,
        )
    ).parsed
