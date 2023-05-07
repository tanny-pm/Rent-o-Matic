from rentomatic.domain.room import Room
from rentomatic.repository.iroomrepo import IRoomRepo


class MemRepo(IRoomRepo):
    def __init__(self, data: list[dict]):
        self.data = data

    def list(self) -> list[Room]:
        return [Room.from_dict(i) for i in self.data]

    def add(self, room: dict) -> int:
        self.data.append(room)
        return 0
