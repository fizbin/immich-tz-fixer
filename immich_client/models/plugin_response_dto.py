from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plugin_action_response_dto import PluginActionResponseDto
    from ..models.plugin_filter_response_dto import PluginFilterResponseDto


T = TypeVar("T", bound="PluginResponseDto")


@_attrs_define
class PluginResponseDto:
    """
    Attributes:
        actions (list[PluginActionResponseDto]):
        author (str):
        created_at (str):
        description (str):
        filters (list[PluginFilterResponseDto]):
        id (str):
        name (str):
        title (str):
        updated_at (str):
        version (str):
    """

    actions: list[PluginActionResponseDto]
    author: str
    created_at: str
    description: str
    filters: list[PluginFilterResponseDto]
    id: str
    name: str
    title: str
    updated_at: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        author = self.author

        created_at = self.created_at

        description = self.description

        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        id = self.id

        name = self.name

        title = self.title

        updated_at = self.updated_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
                "author": author,
                "createdAt": created_at,
                "description": description,
                "filters": filters,
                "id": id,
                "name": name,
                "title": title,
                "updatedAt": updated_at,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_action_response_dto import PluginActionResponseDto
        from ..models.plugin_filter_response_dto import PluginFilterResponseDto

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = PluginActionResponseDto.from_dict(actions_item_data)

            actions.append(actions_item)

        author = d.pop("author")

        created_at = d.pop("createdAt")

        description = d.pop("description")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = PluginFilterResponseDto.from_dict(filters_item_data)

            filters.append(filters_item)

        id = d.pop("id")

        name = d.pop("name")

        title = d.pop("title")

        updated_at = d.pop("updatedAt")

        version = d.pop("version")

        plugin_response_dto = cls(
            actions=actions,
            author=author,
            created_at=created_at,
            description=description,
            filters=filters,
            id=id,
            name=name,
            title=title,
            updated_at=updated_at,
            version=version,
        )

        plugin_response_dto.additional_properties = d
        return plugin_response_dto

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
