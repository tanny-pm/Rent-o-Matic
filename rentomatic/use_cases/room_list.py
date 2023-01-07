from rentomatic.domain.room import Room
from rentomatic.repository.iroomrepo import IRoomRepo


def room_list_use_case(repo: IRoomRepo) -> list[Room]:
    """Get list of all Rooms"""
    return repo.list()


def room_price_all_use_case(repo: IRoomRepo) -> int:
    """Get sum of all room prices"""
    total = 0
    rooms = repo.list()

    for r in rooms:
        total += r.price
    return total
