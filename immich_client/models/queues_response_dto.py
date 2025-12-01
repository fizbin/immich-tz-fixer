from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.queue_response_dto import QueueResponseDto


T = TypeVar("T", bound="QueuesResponseDto")


@_attrs_define
class QueuesResponseDto:
    """
    Attributes:
        background_task (QueueResponseDto):
        backup_database (QueueResponseDto):
        duplicate_detection (QueueResponseDto):
        face_detection (QueueResponseDto):
        facial_recognition (QueueResponseDto):
        library (QueueResponseDto):
        metadata_extraction (QueueResponseDto):
        migration (QueueResponseDto):
        notifications (QueueResponseDto):
        ocr (QueueResponseDto):
        search (QueueResponseDto):
        sidecar (QueueResponseDto):
        smart_search (QueueResponseDto):
        storage_template_migration (QueueResponseDto):
        thumbnail_generation (QueueResponseDto):
        video_conversion (QueueResponseDto):
        workflow (QueueResponseDto):
    """

    background_task: QueueResponseDto
    backup_database: QueueResponseDto
    duplicate_detection: QueueResponseDto
    face_detection: QueueResponseDto
    facial_recognition: QueueResponseDto
    library: QueueResponseDto
    metadata_extraction: QueueResponseDto
    migration: QueueResponseDto
    notifications: QueueResponseDto
    ocr: QueueResponseDto
    search: QueueResponseDto
    sidecar: QueueResponseDto
    smart_search: QueueResponseDto
    storage_template_migration: QueueResponseDto
    thumbnail_generation: QueueResponseDto
    video_conversion: QueueResponseDto
    workflow: QueueResponseDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background_task = self.background_task.to_dict()

        backup_database = self.backup_database.to_dict()

        duplicate_detection = self.duplicate_detection.to_dict()

        face_detection = self.face_detection.to_dict()

        facial_recognition = self.facial_recognition.to_dict()

        library = self.library.to_dict()

        metadata_extraction = self.metadata_extraction.to_dict()

        migration = self.migration.to_dict()

        notifications = self.notifications.to_dict()

        ocr = self.ocr.to_dict()

        search = self.search.to_dict()

        sidecar = self.sidecar.to_dict()

        smart_search = self.smart_search.to_dict()

        storage_template_migration = self.storage_template_migration.to_dict()

        thumbnail_generation = self.thumbnail_generation.to_dict()

        video_conversion = self.video_conversion.to_dict()

        workflow = self.workflow.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backgroundTask": background_task,
                "backupDatabase": backup_database,
                "duplicateDetection": duplicate_detection,
                "faceDetection": face_detection,
                "facialRecognition": facial_recognition,
                "library": library,
                "metadataExtraction": metadata_extraction,
                "migration": migration,
                "notifications": notifications,
                "ocr": ocr,
                "search": search,
                "sidecar": sidecar,
                "smartSearch": smart_search,
                "storageTemplateMigration": storage_template_migration,
                "thumbnailGeneration": thumbnail_generation,
                "videoConversion": video_conversion,
                "workflow": workflow,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.queue_response_dto import QueueResponseDto

        d = dict(src_dict)
        background_task = QueueResponseDto.from_dict(d.pop("backgroundTask"))

        backup_database = QueueResponseDto.from_dict(d.pop("backupDatabase"))

        duplicate_detection = QueueResponseDto.from_dict(d.pop("duplicateDetection"))

        face_detection = QueueResponseDto.from_dict(d.pop("faceDetection"))

        facial_recognition = QueueResponseDto.from_dict(d.pop("facialRecognition"))

        library = QueueResponseDto.from_dict(d.pop("library"))

        metadata_extraction = QueueResponseDto.from_dict(d.pop("metadataExtraction"))

        migration = QueueResponseDto.from_dict(d.pop("migration"))

        notifications = QueueResponseDto.from_dict(d.pop("notifications"))

        ocr = QueueResponseDto.from_dict(d.pop("ocr"))

        search = QueueResponseDto.from_dict(d.pop("search"))

        sidecar = QueueResponseDto.from_dict(d.pop("sidecar"))

        smart_search = QueueResponseDto.from_dict(d.pop("smartSearch"))

        storage_template_migration = QueueResponseDto.from_dict(d.pop("storageTemplateMigration"))

        thumbnail_generation = QueueResponseDto.from_dict(d.pop("thumbnailGeneration"))

        video_conversion = QueueResponseDto.from_dict(d.pop("videoConversion"))

        workflow = QueueResponseDto.from_dict(d.pop("workflow"))

        queues_response_dto = cls(
            background_task=background_task,
            backup_database=backup_database,
            duplicate_detection=duplicate_detection,
            face_detection=face_detection,
            facial_recognition=facial_recognition,
            library=library,
            metadata_extraction=metadata_extraction,
            migration=migration,
            notifications=notifications,
            ocr=ocr,
            search=search,
            sidecar=sidecar,
            smart_search=smart_search,
            storage_template_migration=storage_template_migration,
            thumbnail_generation=thumbnail_generation,
            video_conversion=video_conversion,
            workflow=workflow,
        )

        queues_response_dto.additional_properties = d
        return queues_response_dto

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
