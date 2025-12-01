from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_avatar_color import UserAvatarColor

T = TypeVar("T", bound="SyncAuthUserV1")


@_attrs_define
class SyncAuthUserV1:
    """
    Attributes:
        avatar_color (None | UserAvatarColor):
        deleted_at (datetime.datetime | None):
        email (str):
        has_profile_image (bool):
        id (str):
        is_admin (bool):
        name (str):
        oauth_id (str):
        pin_code (None | str):
        profile_changed_at (datetime.datetime):
        quota_size_in_bytes (int | None):
        quota_usage_in_bytes (int):
        storage_label (None | str):
    """

    avatar_color: None | UserAvatarColor
    deleted_at: datetime.datetime | None
    email: str
    has_profile_image: bool
    id: str
    is_admin: bool
    name: str
    oauth_id: str
    pin_code: None | str
    profile_changed_at: datetime.datetime
    quota_size_in_bytes: int | None
    quota_usage_in_bytes: int
    storage_label: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_color: None | str
        if isinstance(self.avatar_color, UserAvatarColor):
            avatar_color = self.avatar_color.value
        else:
            avatar_color = self.avatar_color

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        email = self.email

        has_profile_image = self.has_profile_image

        id = self.id

        is_admin = self.is_admin

        name = self.name

        oauth_id = self.oauth_id

        pin_code: None | str
        pin_code = self.pin_code

        profile_changed_at = self.profile_changed_at.isoformat()

        quota_size_in_bytes: int | None
        quota_size_in_bytes = self.quota_size_in_bytes

        quota_usage_in_bytes = self.quota_usage_in_bytes

        storage_label: None | str
        storage_label = self.storage_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatarColor": avatar_color,
                "deletedAt": deleted_at,
                "email": email,
                "hasProfileImage": has_profile_image,
                "id": id,
                "isAdmin": is_admin,
                "name": name,
                "oauthId": oauth_id,
                "pinCode": pin_code,
                "profileChangedAt": profile_changed_at,
                "quotaSizeInBytes": quota_size_in_bytes,
                "quotaUsageInBytes": quota_usage_in_bytes,
                "storageLabel": storage_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_avatar_color(data: object) -> None | UserAvatarColor:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                avatar_color_type_1 = UserAvatarColor(data)

                return avatar_color_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserAvatarColor, data)

        avatar_color = _parse_avatar_color(d.pop("avatarColor"))

        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))

        email = d.pop("email")

        has_profile_image = d.pop("hasProfileImage")

        id = d.pop("id")

        is_admin = d.pop("isAdmin")

        name = d.pop("name")

        oauth_id = d.pop("oauthId")

        def _parse_pin_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pin_code = _parse_pin_code(d.pop("pinCode"))

        profile_changed_at = isoparse(d.pop("profileChangedAt"))

        def _parse_quota_size_in_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        quota_size_in_bytes = _parse_quota_size_in_bytes(d.pop("quotaSizeInBytes"))

        quota_usage_in_bytes = d.pop("quotaUsageInBytes")

        def _parse_storage_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        storage_label = _parse_storage_label(d.pop("storageLabel"))

        sync_auth_user_v1 = cls(
            avatar_color=avatar_color,
            deleted_at=deleted_at,
            email=email,
            has_profile_image=has_profile_image,
            id=id,
            is_admin=is_admin,
            name=name,
            oauth_id=oauth_id,
            pin_code=pin_code,
            profile_changed_at=profile_changed_at,
            quota_size_in_bytes=quota_size_in_bytes,
            quota_usage_in_bytes=quota_usage_in_bytes,
            storage_label=storage_label,
        )

        sync_auth_user_v1.additional_properties = d
        return sync_auth_user_v1

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
