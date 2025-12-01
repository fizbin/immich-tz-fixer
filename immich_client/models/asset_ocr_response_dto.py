from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetOcrResponseDto")


@_attrs_define
class AssetOcrResponseDto:
    """
    Attributes:
        asset_id (UUID):
        box_score (float): Confidence score for text detection box
        id (UUID):
        text (str): Recognized text
        text_score (float): Confidence score for text recognition
        x1 (float): Normalized x coordinate of box corner 1 (0-1)
        x2 (float): Normalized x coordinate of box corner 2 (0-1)
        x3 (float): Normalized x coordinate of box corner 3 (0-1)
        x4 (float): Normalized x coordinate of box corner 4 (0-1)
        y1 (float): Normalized y coordinate of box corner 1 (0-1)
        y2 (float): Normalized y coordinate of box corner 2 (0-1)
        y3 (float): Normalized y coordinate of box corner 3 (0-1)
        y4 (float): Normalized y coordinate of box corner 4 (0-1)
    """

    asset_id: UUID
    box_score: float
    id: UUID
    text: str
    text_score: float
    x1: float
    x2: float
    x3: float
    x4: float
    y1: float
    y2: float
    y3: float
    y4: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        box_score = self.box_score

        id = str(self.id)

        text = self.text

        text_score = self.text_score

        x1 = self.x1

        x2 = self.x2

        x3 = self.x3

        x4 = self.x4

        y1 = self.y1

        y2 = self.y2

        y3 = self.y3

        y4 = self.y4

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "boxScore": box_score,
                "id": id,
                "text": text,
                "textScore": text_score,
                "x1": x1,
                "x2": x2,
                "x3": x3,
                "x4": x4,
                "y1": y1,
                "y2": y2,
                "y3": y3,
                "y4": y4,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("assetId"))

        box_score = d.pop("boxScore")

        id = UUID(d.pop("id"))

        text = d.pop("text")

        text_score = d.pop("textScore")

        x1 = d.pop("x1")

        x2 = d.pop("x2")

        x3 = d.pop("x3")

        x4 = d.pop("x4")

        y1 = d.pop("y1")

        y2 = d.pop("y2")

        y3 = d.pop("y3")

        y4 = d.pop("y4")

        asset_ocr_response_dto = cls(
            asset_id=asset_id,
            box_score=box_score,
            id=id,
            text=text,
            text_score=text_score,
            x1=x1,
            x2=x2,
            x3=x3,
            x4=x4,
            y1=y1,
            y2=y2,
            y3=y3,
            y4=y4,
        )

        asset_ocr_response_dto.additional_properties = d
        return asset_ocr_response_dto

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
