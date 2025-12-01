from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.shared_link_type import SharedLinkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_response_dto import AlbumResponseDto
    from ..models.asset_response_dto import AssetResponseDto


T = TypeVar("T", bound="SharedLinkResponseDto")


@_attrs_define
class SharedLinkResponseDto:
    """
    Attributes:
        allow_download (bool):
        allow_upload (bool):
        assets (list[AssetResponseDto]):
        created_at (datetime.datetime):
        description (None | str):
        expires_at (datetime.datetime | None):
        id (str):
        key (str):
        password (None | str):
        show_metadata (bool):
        slug (None | str):
        type_ (SharedLinkType):
        user_id (str):
        album (AlbumResponseDto | Unset):
        token (None | str | Unset):
    """

    allow_download: bool
    allow_upload: bool
    assets: list[AssetResponseDto]
    created_at: datetime.datetime
    description: None | str
    expires_at: datetime.datetime | None
    id: str
    key: str
    password: None | str
    show_metadata: bool
    slug: None | str
    type_: SharedLinkType
    user_id: str
    album: AlbumResponseDto | Unset = UNSET
    token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_download = self.allow_download

        allow_upload = self.allow_upload

        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        created_at = self.created_at.isoformat()

        description: None | str
        description = self.description

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        id = self.id

        key = self.key

        password: None | str
        password = self.password

        show_metadata = self.show_metadata

        slug: None | str
        slug = self.slug

        type_ = self.type_.value

        user_id = self.user_id

        album: dict[str, Any] | Unset = UNSET
        if not isinstance(self.album, Unset):
            album = self.album.to_dict()

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowDownload": allow_download,
                "allowUpload": allow_upload,
                "assets": assets,
                "createdAt": created_at,
                "description": description,
                "expiresAt": expires_at,
                "id": id,
                "key": key,
                "password": password,
                "showMetadata": show_metadata,
                "slug": slug,
                "type": type_,
                "userId": user_id,
            }
        )
        if album is not UNSET:
            field_dict["album"] = album
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_response_dto import AlbumResponseDto
        from ..models.asset_response_dto import AssetResponseDto

        d = dict(src_dict)
        allow_download = d.pop("allowDownload")

        allow_upload = d.pop("allowUpload")

        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = AssetResponseDto.from_dict(assets_item_data)

            assets.append(assets_item)

        created_at = isoparse(d.pop("createdAt"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        id = d.pop("id")

        key = d.pop("key")

        def _parse_password(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        password = _parse_password(d.pop("password"))

        show_metadata = d.pop("showMetadata")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        type_ = SharedLinkType(d.pop("type"))

        user_id = d.pop("userId")

        _album = d.pop("album", UNSET)
        album: AlbumResponseDto | Unset
        if isinstance(_album, Unset):
            album = UNSET
        else:
            album = AlbumResponseDto.from_dict(_album)

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

        shared_link_response_dto = cls(
            allow_download=allow_download,
            allow_upload=allow_upload,
            assets=assets,
            created_at=created_at,
            description=description,
            expires_at=expires_at,
            id=id,
            key=key,
            password=password,
            show_metadata=show_metadata,
            slug=slug,
            type_=type_,
            user_id=user_id,
            album=album,
            token=token,
        )

        shared_link_response_dto.additional_properties = d
        return shared_link_response_dto

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
