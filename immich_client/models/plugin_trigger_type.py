from enum import Enum


class PluginTriggerType(str, Enum):
    ASSETCREATE = "AssetCreate"
    PERSONRECOGNIZED = "PersonRecognized"

    def __str__(self) -> str:
        return str(self.value)
