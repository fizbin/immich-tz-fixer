from enum import Enum


class WorkflowResponseDtoTriggerType(str, Enum):
    ASSETCREATE = "AssetCreate"
    PERSONRECOGNIZED = "PersonRecognized"

    def __str__(self) -> str:
        return str(self.value)
