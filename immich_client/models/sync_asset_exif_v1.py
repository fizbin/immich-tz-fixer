from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SyncAssetExifV1")


@_attrs_define
class SyncAssetExifV1:
    """
    Attributes:
        asset_id (str):
        city (None | str):
        country (None | str):
        date_time_original (datetime.datetime | None):
        description (None | str):
        exif_image_height (int | None):
        exif_image_width (int | None):
        exposure_time (None | str):
        f_number (float | None):
        file_size_in_byte (int | None):
        focal_length (float | None):
        fps (float | None):
        iso (int | None):
        latitude (float | None):
        lens_model (None | str):
        longitude (float | None):
        make (None | str):
        model (None | str):
        modify_date (datetime.datetime | None):
        orientation (None | str):
        profile_description (None | str):
        projection_type (None | str):
        rating (int | None):
        state (None | str):
        time_zone (None | str):
    """

    asset_id: str
    city: None | str
    country: None | str
    date_time_original: datetime.datetime | None
    description: None | str
    exif_image_height: int | None
    exif_image_width: int | None
    exposure_time: None | str
    f_number: float | None
    file_size_in_byte: int | None
    focal_length: float | None
    fps: float | None
    iso: int | None
    latitude: float | None
    lens_model: None | str
    longitude: float | None
    make: None | str
    model: None | str
    modify_date: datetime.datetime | None
    orientation: None | str
    profile_description: None | str
    projection_type: None | str
    rating: int | None
    state: None | str
    time_zone: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        city: None | str
        city = self.city

        country: None | str
        country = self.country

        date_time_original: None | str
        if isinstance(self.date_time_original, datetime.datetime):
            date_time_original = self.date_time_original.isoformat()
        else:
            date_time_original = self.date_time_original

        description: None | str
        description = self.description

        exif_image_height: int | None
        exif_image_height = self.exif_image_height

        exif_image_width: int | None
        exif_image_width = self.exif_image_width

        exposure_time: None | str
        exposure_time = self.exposure_time

        f_number: float | None
        f_number = self.f_number

        file_size_in_byte: int | None
        file_size_in_byte = self.file_size_in_byte

        focal_length: float | None
        focal_length = self.focal_length

        fps: float | None
        fps = self.fps

        iso: int | None
        iso = self.iso

        latitude: float | None
        latitude = self.latitude

        lens_model: None | str
        lens_model = self.lens_model

        longitude: float | None
        longitude = self.longitude

        make: None | str
        make = self.make

        model: None | str
        model = self.model

        modify_date: None | str
        if isinstance(self.modify_date, datetime.datetime):
            modify_date = self.modify_date.isoformat()
        else:
            modify_date = self.modify_date

        orientation: None | str
        orientation = self.orientation

        profile_description: None | str
        profile_description = self.profile_description

        projection_type: None | str
        projection_type = self.projection_type

        rating: int | None
        rating = self.rating

        state: None | str
        state = self.state

        time_zone: None | str
        time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "city": city,
                "country": country,
                "dateTimeOriginal": date_time_original,
                "description": description,
                "exifImageHeight": exif_image_height,
                "exifImageWidth": exif_image_width,
                "exposureTime": exposure_time,
                "fNumber": f_number,
                "fileSizeInByte": file_size_in_byte,
                "focalLength": focal_length,
                "fps": fps,
                "iso": iso,
                "latitude": latitude,
                "lensModel": lens_model,
                "longitude": longitude,
                "make": make,
                "model": model,
                "modifyDate": modify_date,
                "orientation": orientation,
                "profileDescription": profile_description,
                "projectionType": projection_type,
                "rating": rating,
                "state": state,
                "timeZone": time_zone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("assetId")

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_date_time_original(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_time_original_type_0 = isoparse(data)

                return date_time_original_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_time_original = _parse_date_time_original(d.pop("dateTimeOriginal"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_exif_image_height(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        exif_image_height = _parse_exif_image_height(d.pop("exifImageHeight"))

        def _parse_exif_image_width(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        exif_image_width = _parse_exif_image_width(d.pop("exifImageWidth"))

        def _parse_exposure_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        exposure_time = _parse_exposure_time(d.pop("exposureTime"))

        def _parse_f_number(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        f_number = _parse_f_number(d.pop("fNumber"))

        def _parse_file_size_in_byte(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        file_size_in_byte = _parse_file_size_in_byte(d.pop("fileSizeInByte"))

        def _parse_focal_length(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        focal_length = _parse_focal_length(d.pop("focalLength"))

        def _parse_fps(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        fps = _parse_fps(d.pop("fps"))

        def _parse_iso(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        iso = _parse_iso(d.pop("iso"))

        def _parse_latitude(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        latitude = _parse_latitude(d.pop("latitude"))

        def _parse_lens_model(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        lens_model = _parse_lens_model(d.pop("lensModel"))

        def _parse_longitude(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        longitude = _parse_longitude(d.pop("longitude"))

        def _parse_make(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        make = _parse_make(d.pop("make"))

        def _parse_model(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model = _parse_model(d.pop("model"))

        def _parse_modify_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modify_date_type_0 = isoparse(data)

                return modify_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        modify_date = _parse_modify_date(d.pop("modifyDate"))

        def _parse_orientation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        orientation = _parse_orientation(d.pop("orientation"))

        def _parse_profile_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_description = _parse_profile_description(d.pop("profileDescription"))

        def _parse_projection_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        projection_type = _parse_projection_type(d.pop("projectionType"))

        def _parse_rating(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rating = _parse_rating(d.pop("rating"))

        def _parse_state(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state = _parse_state(d.pop("state"))

        def _parse_time_zone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        time_zone = _parse_time_zone(d.pop("timeZone"))

        sync_asset_exif_v1 = cls(
            asset_id=asset_id,
            city=city,
            country=country,
            date_time_original=date_time_original,
            description=description,
            exif_image_height=exif_image_height,
            exif_image_width=exif_image_width,
            exposure_time=exposure_time,
            f_number=f_number,
            file_size_in_byte=file_size_in_byte,
            focal_length=focal_length,
            fps=fps,
            iso=iso,
            latitude=latitude,
            lens_model=lens_model,
            longitude=longitude,
            make=make,
            model=model,
            modify_date=modify_date,
            orientation=orientation,
            profile_description=profile_description,
            projection_type=projection_type,
            rating=rating,
            state=state,
            time_zone=time_zone,
        )

        sync_asset_exif_v1.additional_properties = d
        return sync_asset_exif_v1

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
