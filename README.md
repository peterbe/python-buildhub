# python-buildhub

[![Build Status](https://travis-ci.org/peterbe/python-buildhub.svg?branch=master)](https://travis-ci.org/peterbe/python-buildhub)
[![Code style](https://img.shields.io/badge/Code%20style-black-000000.svg)](https://github.com/ambv/black)

A simple wrapper on the Buildhub service. Basically, a glorified
Elasticsearch over HTTP wrapper.

## WORD OF WARNING

**This is an experimental project, and the API is to be considered a prototype.**

It's production-grade in terms of functionality (because it's so simple), but
not only might things change but also consider it very minimal in features
which means it can get better if you help out.

## Install and Usage

Requires Python 3.

```bash
pip install python-buildhub
```

```python
from buildhub import get_distinct_versions, get_distinct_buildids

print(get_distinct_versions(
    # product="Firefox",
    # channel="beta",
    # startswith="64",
))

print(get_distinct_buildids(
    # product="Firefox",
    # channel="beta",
    # startswith="2018",
))
```

If you want to use a different URL for the backend there are two ways to override it:

```bash
$ export BUILDHUB_SEARCH_URL=http://localhost:8888/api/search
$ python -c 'import buildhub; print(buildhub.SEARCH_URL)'
http://localhost:8888/api/search
```

or

```python
from buildhub import get_distinct_versions

print(get_distinct_versions(
    _search_url='http://localhost:8000/api/v1'
))
```

Considering that this project is just a wrapper for making a Elasticsearch search
query in JSON over HTTP POST, if you want to know what query gets sent you can use:

```python
from buildhub import get_distinct_versions

get_distinct_versions(_verbose=True)
```

...and it will print the JSON used on `stdout`.

## Contributing

Clone repo, create an environment and run:

```bash
pip install -e ".[dev]"
```

To get automatic `flake8` and `black` checking done in a git pre-commit
hook run:

```bash
therapist install
```

## License

Delivery Console is licensed under the MPLv2. See the
[LICENSE](LICENSE) file for details.
