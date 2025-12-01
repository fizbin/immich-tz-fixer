from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedLinkEditDto")


@_attrs_define
class SharedLinkEditDto:
    """
    Attributes:
        allow_download (bool | Unset):
        allow_upload (bool | Unset):
        change_expiry_time (bool | Unset): Few clients cannot send null to set the expiryTime to never.
            Setting this flag and not sending expiryAt is considered as null instead.
            Clients that can send null values can ignore this.
        description (None | str | Unset):
        expires_at (datetime.datetime | None | Unset):
        password (None | str | Unset):
        show_metadata (bool | Unset):
        slug (None | str | Unset):
    """

    allow_download: bool | Unset = UNSET
    allow_upload: bool | Unset = UNSET
    change_expiry_time: bool | Unset = UNSET
    description: None | str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    password: None | str | Unset = UNSET
    show_metadata: bool | Unset = UNSET
    slug: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_download = self.allow_download

        allow_upload = self.allow_upload

        change_expiry_time = self.change_expiry_time

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        show_metadata = self.show_metadata

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_download is not UNSET:
            field_dict["allowDownload"] = allow_download
        if allow_upload is not UNSET:
            field_dict["allowUpload"] = allow_upload
        if change_expiry_time is not UNSET:
            field_dict["changeExpiryTime"] = change_expiry_time
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if password is not UNSET:
            field_dict["password"] = password
        if show_metadata is not UNSET:
            field_dict["showMetadata"] = show_metadata
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_download = d.pop("allowDownload", UNSET)

        allow_upload = d.pop("allowUpload", UNSET)

        change_expiry_time = d.pop("changeExpiryTime", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        show_metadata = d.pop("showMetadata", UNSET)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        shared_link_edit_dto = cls(
            allow_download=allow_download,
            allow_upload=allow_upload,
            change_expiry_time=change_expiry_time,
            description=description,
            expires_at=expires_at,
            password=password,
            show_metadata=show_metadata,
            slug=slug,
        )

        shared_link_edit_dto.additional_properties = d
        return shared_link_edit_dto

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
