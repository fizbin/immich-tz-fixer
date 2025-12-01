from enum import Enum


class QueueName(str, Enum):
    BACKGROUNDTASK = "backgroundTask"
    BACKUPDATABASE = "backupDatabase"
    DUPLICATEDETECTION = "duplicateDetection"
    FACEDETECTION = "faceDetection"
    FACIALRECOGNITION = "facialRecognition"
    LIBRARY = "library"
    METADATAEXTRACTION = "metadataExtraction"
    MIGRATION = "migration"
    NOTIFICATIONS = "notifications"
    OCR = "ocr"
    SEARCH = "search"
    SIDECAR = "sidecar"
    SMARTSEARCH = "smartSearch"
    STORAGETEMPLATEMIGRATION = "storageTemplateMigration"
    THUMBNAILGENERATION = "thumbnailGeneration"
    VIDEOCONVERSION = "videoConversion"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
