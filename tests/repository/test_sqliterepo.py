import pytest

from rentomatic.domain.room import Room
from rentomatic.repository.sqliterepo import SqliteRepo


@pytest.fixture
def room_dicts():
    return [
        {
            "code": "1111",
            "size": 215,
            "price": 39,
            "longitude": -0.09998975,
            "latitude": 51.75436293,
        },
        {
            "code": "2222",
            "size": 405,
            "price": 66,
            "longitude": 0.18228006,
            "latitude": 51.74640997,
        },
        {
            "code": "3333",
            "size": 56,
            "price": 60,
            "longitude": 0.27891577,
            "latitude": 51.45994069,
        },
        {
            "code": "4444",
            "size": 93,
            "price": 48,
            "longitude": 0.33894476,
            "latitude": 51.39916678,
        },
    ]


def test_repository_list_without_parameters(room_dicts):
    repo = SqliteRepo("rentomatic.db")

    rooms = [Room.from_dict(i) for i in room_dicts]

    assert repo.list() == rooms


def test_repository_add(room_dicts):
    # 未実装
    pass
