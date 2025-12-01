from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plugin_trigger_type import PluginTriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_action_item_dto import WorkflowActionItemDto
    from ..models.workflow_filter_item_dto import WorkflowFilterItemDto


T = TypeVar("T", bound="WorkflowCreateDto")


@_attrs_define
class WorkflowCreateDto:
    """
    Attributes:
        actions (list[WorkflowActionItemDto]):
        filters (list[WorkflowFilterItemDto]):
        name (str):
        trigger_type (PluginTriggerType):
        description (str | Unset):
        enabled (bool | Unset):
    """

    actions: list[WorkflowActionItemDto]
    filters: list[WorkflowFilterItemDto]
    name: str
    trigger_type: PluginTriggerType
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        name = self.name

        trigger_type = self.trigger_type.value

        description = self.description

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
                "filters": filters,
                "name": name,
                "triggerType": trigger_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_action_item_dto import WorkflowActionItemDto
        from ..models.workflow_filter_item_dto import WorkflowFilterItemDto

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = WorkflowActionItemDto.from_dict(actions_item_data)

            actions.append(actions_item)

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = WorkflowFilterItemDto.from_dict(filters_item_data)

            filters.append(filters_item)

        name = d.pop("name")

        trigger_type = PluginTriggerType(d.pop("triggerType"))

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        workflow_create_dto = cls(
            actions=actions,
            filters=filters,
            name=name,
            trigger_type=trigger_type,
            description=description,
            enabled=enabled,
        )

        workflow_create_dto.additional_properties = d
        return workflow_create_dto

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
