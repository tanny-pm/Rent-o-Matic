from rentomatic.domain.room import Room
from rentomatic.repository.iroomrepo import IRoomRepo


class MemRepo(IRoomRepo):
    def __init__(self, data: list[Room]):
        self.data = data

    def list(self):
        return [Room.from_dict(i) for i in self.data]

    def add(self, room):
        self.data.append(room)
        return 0
