from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_action_response_dto_action_config_type_0 import (
        WorkflowActionResponseDtoActionConfigType0,
    )


T = TypeVar("T", bound="WorkflowActionResponseDto")


@_attrs_define
class WorkflowActionResponseDto:
    """
    Attributes:
        action_config (None | WorkflowActionResponseDtoActionConfigType0):
        action_id (str):
        id (str):
        order (float):
        workflow_id (str):
    """

    action_config: None | WorkflowActionResponseDtoActionConfigType0
    action_id: str
    id: str
    order: float
    workflow_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_action_response_dto_action_config_type_0 import (
            WorkflowActionResponseDtoActionConfigType0,
        )

        action_config: dict[str, Any] | None
        if isinstance(self.action_config, WorkflowActionResponseDtoActionConfigType0):
            action_config = self.action_config.to_dict()
        else:
            action_config = self.action_config

        action_id = self.action_id

        id = self.id

        order = self.order

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionConfig": action_config,
                "actionId": action_id,
                "id": id,
                "order": order,
                "workflowId": workflow_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_action_response_dto_action_config_type_0 import (
            WorkflowActionResponseDtoActionConfigType0,
        )

        d = dict(src_dict)

        def _parse_action_config(
            data: object,
        ) -> None | WorkflowActionResponseDtoActionConfigType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_config_type_0 = WorkflowActionResponseDtoActionConfigType0.from_dict(data)

                return action_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkflowActionResponseDtoActionConfigType0, data)

        action_config = _parse_action_config(d.pop("actionConfig"))

        action_id = d.pop("actionId")

        id = d.pop("id")

        order = d.pop("order")

        workflow_id = d.pop("workflowId")

        workflow_action_response_dto = cls(
            action_config=action_config,
            action_id=action_id,
            id=id,
            order=order,
            workflow_id=workflow_id,
        )

        workflow_action_response_dto.additional_properties = d
        return workflow_action_response_dto

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
