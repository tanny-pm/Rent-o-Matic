#!/usr/bin/env python

from rentomatic.repository.sqliterepo import SqliteRepo
from rentomatic.use_cases.room_list import room_list_use_case

repo = SqliteRepo("rentomatic.db")
result = room_list_use_case(repo)

print([room.to_dict() for room in result])
