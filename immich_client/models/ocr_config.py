from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OcrConfig")


@_attrs_define
class OcrConfig:
    """
    Attributes:
        enabled (bool):
        max_resolution (int):
        min_detection_score (float):
        min_recognition_score (float):
        model_name (str):
    """

    enabled: bool
    max_resolution: int
    min_detection_score: float
    min_recognition_score: float
    model_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        max_resolution = self.max_resolution

        min_detection_score = self.min_detection_score

        min_recognition_score = self.min_recognition_score

        model_name = self.model_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "maxResolution": max_resolution,
                "minDetectionScore": min_detection_score,
                "minRecognitionScore": min_recognition_score,
                "modelName": model_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        max_resolution = d.pop("maxResolution")

        min_detection_score = d.pop("minDetectionScore")

        min_recognition_score = d.pop("minRecognitionScore")

        model_name = d.pop("modelName")

        ocr_config = cls(
            enabled=enabled,
            max_resolution=max_resolution,
            min_detection_score=min_detection_score,
            min_recognition_score=min_recognition_score,
            model_name=model_name,
        )

        ocr_config.additional_properties = d
        return ocr_config

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
