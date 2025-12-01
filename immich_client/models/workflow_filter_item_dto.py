from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_filter_item_dto_filter_config import (
        WorkflowFilterItemDtoFilterConfig,
    )


T = TypeVar("T", bound="WorkflowFilterItemDto")


@_attrs_define
class WorkflowFilterItemDto:
    """
    Attributes:
        filter_id (UUID):
        filter_config (WorkflowFilterItemDtoFilterConfig | Unset):
    """

    filter_id: UUID
    filter_config: WorkflowFilterItemDtoFilterConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_id = str(self.filter_id)

        filter_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_config, Unset):
            filter_config = self.filter_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filterId": filter_id,
            }
        )
        if filter_config is not UNSET:
            field_dict["filterConfig"] = filter_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_filter_item_dto_filter_config import (
            WorkflowFilterItemDtoFilterConfig,
        )

        d = dict(src_dict)
        filter_id = UUID(d.pop("filterId"))

        _filter_config = d.pop("filterConfig", UNSET)
        filter_config: WorkflowFilterItemDtoFilterConfig | Unset
        if isinstance(_filter_config, Unset):
            filter_config = UNSET
        else:
            filter_config = WorkflowFilterItemDtoFilterConfig.from_dict(_filter_config)

        workflow_filter_item_dto = cls(
            filter_id=filter_id,
            filter_config=filter_config,
        )

        workflow_filter_item_dto.additional_properties = d
        return workflow_filter_item_dto

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
