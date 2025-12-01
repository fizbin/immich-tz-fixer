from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetCopyDto")


@_attrs_define
class AssetCopyDto:
    """
    Attributes:
        source_id (UUID):
        target_id (UUID):
        albums (bool | Unset):  Default: True.
        favorite (bool | Unset):  Default: True.
        shared_links (bool | Unset):  Default: True.
        sidecar (bool | Unset):  Default: True.
        stack (bool | Unset):  Default: True.
    """

    source_id: UUID
    target_id: UUID
    albums: bool | Unset = True
    favorite: bool | Unset = True
    shared_links: bool | Unset = True
    sidecar: bool | Unset = True
    stack: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_id = str(self.source_id)

        target_id = str(self.target_id)

        albums = self.albums

        favorite = self.favorite

        shared_links = self.shared_links

        sidecar = self.sidecar

        stack = self.stack

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceId": source_id,
                "targetId": target_id,
            }
        )
        if albums is not UNSET:
            field_dict["albums"] = albums
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if shared_links is not UNSET:
            field_dict["sharedLinks"] = shared_links
        if sidecar is not UNSET:
            field_dict["sidecar"] = sidecar
        if stack is not UNSET:
            field_dict["stack"] = stack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_id = UUID(d.pop("sourceId"))

        target_id = UUID(d.pop("targetId"))

        albums = d.pop("albums", UNSET)

        favorite = d.pop("favorite", UNSET)

        shared_links = d.pop("sharedLinks", UNSET)

        sidecar = d.pop("sidecar", UNSET)

        stack = d.pop("stack", UNSET)

        asset_copy_dto = cls(
            source_id=source_id,
            target_id=target_id,
            albums=albums,
            favorite=favorite,
            shared_links=shared_links,
            sidecar=sidecar,
            stack=stack,
        )

        asset_copy_dto.additional_properties = d
        return asset_copy_dto

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
