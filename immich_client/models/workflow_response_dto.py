from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_response_dto_trigger_type import WorkflowResponseDtoTriggerType

if TYPE_CHECKING:
    from ..models.workflow_action_response_dto import WorkflowActionResponseDto
    from ..models.workflow_filter_response_dto import WorkflowFilterResponseDto


T = TypeVar("T", bound="WorkflowResponseDto")


@_attrs_define
class WorkflowResponseDto:
    """
    Attributes:
        actions (list[WorkflowActionResponseDto]):
        created_at (str):
        description (str):
        enabled (bool):
        filters (list[WorkflowFilterResponseDto]):
        id (str):
        name (None | str):
        owner_id (str):
        trigger_type (WorkflowResponseDtoTriggerType):
    """

    actions: list[WorkflowActionResponseDto]
    created_at: str
    description: str
    enabled: bool
    filters: list[WorkflowFilterResponseDto]
    id: str
    name: None | str
    owner_id: str
    trigger_type: WorkflowResponseDtoTriggerType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        created_at = self.created_at

        description = self.description

        enabled = self.enabled

        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        id = self.id

        name: None | str
        name = self.name

        owner_id = self.owner_id

        trigger_type = self.trigger_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
                "createdAt": created_at,
                "description": description,
                "enabled": enabled,
                "filters": filters,
                "id": id,
                "name": name,
                "ownerId": owner_id,
                "triggerType": trigger_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_action_response_dto import WorkflowActionResponseDto
        from ..models.workflow_filter_response_dto import WorkflowFilterResponseDto

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = WorkflowActionResponseDto.from_dict(actions_item_data)

            actions.append(actions_item)

        created_at = d.pop("createdAt")

        description = d.pop("description")

        enabled = d.pop("enabled")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = WorkflowFilterResponseDto.from_dict(filters_item_data)

            filters.append(filters_item)

        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        owner_id = d.pop("ownerId")

        trigger_type = WorkflowResponseDtoTriggerType(d.pop("triggerType"))

        workflow_response_dto = cls(
            actions=actions,
            created_at=created_at,
            description=description,
            enabled=enabled,
            filters=filters,
            id=id,
            name=name,
            owner_id=owner_id,
            trigger_type=trigger_type,
        )

        workflow_response_dto.additional_properties = d
        return workflow_response_dto

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
