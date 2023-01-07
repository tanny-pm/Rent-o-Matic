import abc

from rentomatic.domain.room import Room


class IRoomRepo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list(self) -> list[Room]:
        """すべての部屋のリストを返す"""
        pass
