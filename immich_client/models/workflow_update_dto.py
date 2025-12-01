from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_action_item_dto import WorkflowActionItemDto
    from ..models.workflow_filter_item_dto import WorkflowFilterItemDto


T = TypeVar("T", bound="WorkflowUpdateDto")


@_attrs_define
class WorkflowUpdateDto:
    """
    Attributes:
        actions (list[WorkflowActionItemDto] | Unset):
        description (str | Unset):
        enabled (bool | Unset):
        filters (list[WorkflowFilterItemDto] | Unset):
        name (str | Unset):
    """

    actions: list[WorkflowActionItemDto] | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    filters: list[WorkflowFilterItemDto] | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        description = self.description

        enabled = self.enabled

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filters is not UNSET:
            field_dict["filters"] = filters
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_action_item_dto import WorkflowActionItemDto
        from ..models.workflow_filter_item_dto import WorkflowFilterItemDto

        d = dict(src_dict)
        _actions = d.pop("actions", UNSET)
        actions: list[WorkflowActionItemDto] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = WorkflowActionItemDto.from_dict(actions_item_data)

                actions.append(actions_item)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: list[WorkflowFilterItemDto] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = WorkflowFilterItemDto.from_dict(filters_item_data)

                filters.append(filters_item)

        name = d.pop("name", UNSET)

        workflow_update_dto = cls(
            actions=actions,
            description=description,
            enabled=enabled,
            filters=filters,
            name=name,
        )

        workflow_update_dto.additional_properties = d
        return workflow_update_dto

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
