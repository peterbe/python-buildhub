python-buildhub
===============

A simple wrapper on the Buildhub service. Basically, a glorified
Elasticsearch over HTTP wrapper.


## Install and Usage

Requires Python 3.

```bash
pip install python-buildhub
```

```python
from buildhub import get_distinct_versions

print(get_distinct_versions(
    # product="Firefox",
    # channel="beta",
    # major="64",x
))
```

## Contributing

Clone repo, create an environment and run:

```bash
pip install -e ".[dev]"
```

hack hack hack.


## License

Delivery Console is licensed under the MPLv2. See the
[LICENSE](LICENSE) file for details.
