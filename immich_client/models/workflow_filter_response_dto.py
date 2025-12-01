from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_filter_response_dto_filter_config_type_0 import (
        WorkflowFilterResponseDtoFilterConfigType0,
    )


T = TypeVar("T", bound="WorkflowFilterResponseDto")


@_attrs_define
class WorkflowFilterResponseDto:
    """
    Attributes:
        filter_config (None | WorkflowFilterResponseDtoFilterConfigType0):
        filter_id (str):
        id (str):
        order (float):
        workflow_id (str):
    """

    filter_config: None | WorkflowFilterResponseDtoFilterConfigType0
    filter_id: str
    id: str
    order: float
    workflow_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_filter_response_dto_filter_config_type_0 import (
            WorkflowFilterResponseDtoFilterConfigType0,
        )

        filter_config: dict[str, Any] | None
        if isinstance(self.filter_config, WorkflowFilterResponseDtoFilterConfigType0):
            filter_config = self.filter_config.to_dict()
        else:
            filter_config = self.filter_config

        filter_id = self.filter_id

        id = self.id

        order = self.order

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filterConfig": filter_config,
                "filterId": filter_id,
                "id": id,
                "order": order,
                "workflowId": workflow_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_filter_response_dto_filter_config_type_0 import (
            WorkflowFilterResponseDtoFilterConfigType0,
        )

        d = dict(src_dict)

        def _parse_filter_config(
            data: object,
        ) -> None | WorkflowFilterResponseDtoFilterConfigType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_config_type_0 = WorkflowFilterResponseDtoFilterConfigType0.from_dict(data)

                return filter_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkflowFilterResponseDtoFilterConfigType0, data)

        filter_config = _parse_filter_config(d.pop("filterConfig"))

        filter_id = d.pop("filterId")

        id = d.pop("id")

        order = d.pop("order")

        workflow_id = d.pop("workflowId")

        workflow_filter_response_dto = cls(
            filter_config=filter_config,
            filter_id=filter_id,
            id=id,
            order=order,
            workflow_id=workflow_id,
        )

        workflow_filter_response_dto.additional_properties = d
        return workflow_filter_response_dto

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
