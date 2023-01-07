# Rent-o-Matic

Sample of clean architectures in Python

## Installation

```sh
$ poetry install
$ poetry run pytest
```

## Usage

### CLI

```sh
$ ./cli.py
```

### REST API

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
