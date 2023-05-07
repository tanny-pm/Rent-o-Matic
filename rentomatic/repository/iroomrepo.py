import abc

from rentomatic.domain.room import Room


class IRoomRepo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list(self) -> list[Room]:
        """Get list of all Rooms"""
        pass

    @abc.abstractmethod
    def add(self, room: dict) -> int:
        """Add a new Room"""
        pass
