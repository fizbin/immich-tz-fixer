from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.queue_statistics_dto import QueueStatisticsDto
    from ..models.queue_status_dto import QueueStatusDto


T = TypeVar("T", bound="QueueResponseDto")


@_attrs_define
class QueueResponseDto:
    """
    Attributes:
        job_counts (QueueStatisticsDto):
        queue_status (QueueStatusDto):
    """

    job_counts: QueueStatisticsDto
    queue_status: QueueStatusDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_counts = self.job_counts.to_dict()

        queue_status = self.queue_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobCounts": job_counts,
                "queueStatus": queue_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.queue_statistics_dto import QueueStatisticsDto
        from ..models.queue_status_dto import QueueStatusDto

        d = dict(src_dict)
        job_counts = QueueStatisticsDto.from_dict(d.pop("jobCounts"))

        queue_status = QueueStatusDto.from_dict(d.pop("queueStatus"))

        queue_response_dto = cls(
            job_counts=job_counts,
            queue_status=queue_status,
        )

        queue_response_dto.additional_properties = d
        return queue_response_dto

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
