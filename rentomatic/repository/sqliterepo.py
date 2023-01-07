import sqlite3

from rentomatic.domain.room import Room
from rentomatic.repository.iroomrepo import IRoomRepo


class SqliteRepo(IRoomRepo):
    def __init__(self, dbname: str):
        conn = sqlite3.connect(dbname)
        self.cur = conn.cursor()

    def list(self):
        self.cur.execute("SELECT code, size, price, longitude, latitude FROM room")
        rooms = []
        for row in self.cur:
            rooms.append(Room(str(row[0]), row[1], row[2], row[3], row[4]))
        return rooms

    def add(self, room):
        self.cur.execute(
            f"""
            INSERT INTO room VALUES(
              "{room.code}",
              {room.size},
              {room.price},
              {room.longitude},
              {room.latitude}
            )
            """
        )
        return 0
