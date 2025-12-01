from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangePasswordDto")


@_attrs_define
class ChangePasswordDto:
    """
    Attributes:
        new_password (str):  Example: password.
        password (str):  Example: password.
        invalidate_sessions (bool | Unset):  Default: False.
    """

    new_password: str
    password: str
    invalidate_sessions: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_password = self.new_password

        password = self.password

        invalidate_sessions = self.invalidate_sessions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newPassword": new_password,
                "password": password,
            }
        )
        if invalidate_sessions is not UNSET:
            field_dict["invalidateSessions"] = invalidate_sessions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_password = d.pop("newPassword")

        password = d.pop("password")

        invalidate_sessions = d.pop("invalidateSessions", UNSET)

        change_password_dto = cls(
            new_password=new_password,
            password=password,
            invalidate_sessions=invalidate_sessions,
        )

        change_password_dto.additional_properties = d
        return change_password_dto

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
