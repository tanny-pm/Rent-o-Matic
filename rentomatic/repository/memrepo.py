from rentomatic.domain.room import Room
from rentomatic.repository.iroomrepo import IRoomRepo


class MemRepo(IRoomRepo):
    def __init__(self, data):
        self.data = data

    def list(self):
        return [Room.from_dict(i) for i in self.data]
