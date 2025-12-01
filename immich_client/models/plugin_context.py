from enum import Enum


class PluginContext(str, Enum):
    ALBUM = "album"
    ASSET = "asset"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
