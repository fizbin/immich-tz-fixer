from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plugin_context import PluginContext

if TYPE_CHECKING:
    from ..models.plugin_action_response_dto_schema_type_0 import (
        PluginActionResponseDtoSchemaType0,
    )


T = TypeVar("T", bound="PluginActionResponseDto")


@_attrs_define
class PluginActionResponseDto:
    """
    Attributes:
        description (str):
        id (str):
        method_name (str):
        plugin_id (str):
        schema (None | PluginActionResponseDtoSchemaType0):
        supported_contexts (list[PluginContext]):
        title (str):
    """

    description: str
    id: str
    method_name: str
    plugin_id: str
    schema: None | PluginActionResponseDtoSchemaType0
    supported_contexts: list[PluginContext]
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.plugin_action_response_dto_schema_type_0 import (
            PluginActionResponseDtoSchemaType0,
        )

        description = self.description

        id = self.id

        method_name = self.method_name

        plugin_id = self.plugin_id

        schema: dict[str, Any] | None
        if isinstance(self.schema, PluginActionResponseDtoSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        supported_contexts = []
        for supported_contexts_item_data in self.supported_contexts:
            supported_contexts_item = supported_contexts_item_data.value
            supported_contexts.append(supported_contexts_item)

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "methodName": method_name,
                "pluginId": plugin_id,
                "schema": schema,
                "supportedContexts": supported_contexts,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_action_response_dto_schema_type_0 import (
            PluginActionResponseDtoSchemaType0,
        )

        d = dict(src_dict)
        description = d.pop("description")

        id = d.pop("id")

        method_name = d.pop("methodName")

        plugin_id = d.pop("pluginId")

        def _parse_schema(data: object) -> None | PluginActionResponseDtoSchemaType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = PluginActionResponseDtoSchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PluginActionResponseDtoSchemaType0, data)

        schema = _parse_schema(d.pop("schema"))

        supported_contexts = []
        _supported_contexts = d.pop("supportedContexts")
        for supported_contexts_item_data in _supported_contexts:
            supported_contexts_item = PluginContext(supported_contexts_item_data)

            supported_contexts.append(supported_contexts_item)

        title = d.pop("title")

        plugin_action_response_dto = cls(
            description=description,
            id=id,
            method_name=method_name,
            plugin_id=plugin_id,
            schema=schema,
            supported_contexts=supported_contexts,
            title=title,
        )

        plugin_action_response_dto.additional_properties = d
        return plugin_action_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
