from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_action_item_dto_action_config import (
        WorkflowActionItemDtoActionConfig,
    )


T = TypeVar("T", bound="WorkflowActionItemDto")


@_attrs_define
class WorkflowActionItemDto:
    """
    Attributes:
        action_id (UUID):
        action_config (WorkflowActionItemDtoActionConfig | Unset):
    """

    action_id: UUID
    action_config: WorkflowActionItemDtoActionConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_id = str(self.action_id)

        action_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_config, Unset):
            action_config = self.action_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionId": action_id,
            }
        )
        if action_config is not UNSET:
            field_dict["actionConfig"] = action_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_action_item_dto_action_config import (
            WorkflowActionItemDtoActionConfig,
        )

        d = dict(src_dict)
        action_id = UUID(d.pop("actionId"))

        _action_config = d.pop("actionConfig", UNSET)
        action_config: WorkflowActionItemDtoActionConfig | Unset
        if isinstance(_action_config, Unset):
            action_config = UNSET
        else:
            action_config = WorkflowActionItemDtoActionConfig.from_dict(_action_config)

        workflow_action_item_dto = cls(
            action_id=action_id,
            action_config=action_config,
        )

        workflow_action_item_dto.additional_properties = d
        return workflow_action_item_dto

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
