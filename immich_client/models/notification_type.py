from enum import Enum


class NotificationType(str, Enum):
    ALBUMINVITE = "AlbumInvite"
    ALBUMUPDATE = "AlbumUpdate"
    BACKUPFAILED = "BackupFailed"
    CUSTOM = "Custom"
    JOBFAILED = "JobFailed"
    SYSTEMMESSAGE = "SystemMessage"

    def __str__(self) -> str:
        return str(self.value)
