from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_visibility import AssetVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetBulkUpdateDto")


@_attrs_define
class AssetBulkUpdateDto:
    """
    Attributes:
        ids (list[UUID]):
        date_time_original (str | Unset):
        date_time_relative (float | Unset):
        description (str | Unset):
        duplicate_id (None | str | Unset):
        is_favorite (bool | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        rating (float | Unset):
        time_zone (str | Unset):
        visibility (AssetVisibility | Unset):
    """

    ids: list[UUID]
    date_time_original: str | Unset = UNSET
    date_time_relative: float | Unset = UNSET
    description: str | Unset = UNSET
    duplicate_id: None | str | Unset = UNSET
    is_favorite: bool | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    rating: float | Unset = UNSET
    time_zone: str | Unset = UNSET
    visibility: AssetVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = []
        for ids_item_data in self.ids:
            ids_item = str(ids_item_data)
            ids.append(ids_item)

        date_time_original = self.date_time_original

        date_time_relative = self.date_time_relative

        description = self.description

        duplicate_id: None | str | Unset
        if isinstance(self.duplicate_id, Unset):
            duplicate_id = UNSET
        else:
            duplicate_id = self.duplicate_id

        is_favorite = self.is_favorite

        latitude = self.latitude

        longitude = self.longitude

        rating = self.rating

        time_zone = self.time_zone

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if date_time_original is not UNSET:
            field_dict["dateTimeOriginal"] = date_time_original
        if date_time_relative is not UNSET:
            field_dict["dateTimeRelative"] = date_time_relative
        if description is not UNSET:
            field_dict["description"] = description
        if duplicate_id is not UNSET:
            field_dict["duplicateId"] = duplicate_id
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if rating is not UNSET:
            field_dict["rating"] = rating
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = []
        _ids = d.pop("ids")
        for ids_item_data in _ids:
            ids_item = UUID(ids_item_data)

            ids.append(ids_item)

        date_time_original = d.pop("dateTimeOriginal", UNSET)

        date_time_relative = d.pop("dateTimeRelative", UNSET)

        description = d.pop("description", UNSET)

        def _parse_duplicate_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duplicate_id = _parse_duplicate_id(d.pop("duplicateId", UNSET))

        is_favorite = d.pop("isFavorite", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        rating = d.pop("rating", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: AssetVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = AssetVisibility(_visibility)

        asset_bulk_update_dto = cls(
            ids=ids,
            date_time_original=date_time_original,
            date_time_relative=date_time_relative,
            description=description,
            duplicate_id=duplicate_id,
            is_favorite=is_favorite,
            latitude=latitude,
            longitude=longitude,
            rating=rating,
            time_zone=time_zone,
            visibility=visibility,
        )

        asset_bulk_update_dto.additional_properties = d
        return asset_bulk_update_dto

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
