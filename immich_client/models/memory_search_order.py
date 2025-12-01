from enum import Enum


class MemorySearchOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"
    RANDOM = "random"

    def __str__(self) -> str:
        return str(self.value)
