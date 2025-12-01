from enum import Enum


class MaintenanceAction(str, Enum):
    END = "end"
    START = "start"

    def __str__(self) -> str:
        return str(self.value)
