# Rent-o-Matic

Sample of the Python clean architecture app

## Installation

```sh
$ poetry install
$ poetry run python tools/create_db.py
$ poetry run pytest
```

## Usage

### CLI

MemRepo

```sh
$ poetry run python cli.py
```

SqliteRepo

```sh
$ poetry run python cli_sqlite.py
```

### REST API

MemRepo

```sh
$ poetry shell
$ FLASK_CONFIG="development" flask run
$ curl http://127.0.0.1:5000/rooms
```

---

## References

Clean Architectures in Python

https://www.thedigitalcatbooks.com/pycabook-introduction/

Source

https://github.com/pycabook/rentomatic

The Clean Architecture

https://blog.tai2.net/the_clean_architecture.html
