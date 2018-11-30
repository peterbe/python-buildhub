import pytest
import requests_mock

import buildhub


@pytest.fixture
def requestsmock():
    """Return a context where requests are all mocked.
    Usage::

        def test_something(requestsmock):
            requestsmock.get(
                'https://example.com/path'
                content=b'The content'
            )
            # Do stuff that involves requests.get('http://example.com/path')
    """
    with requests_mock.mock() as m:
        yield m


def test_get_distinct_versions(requestsmock):
    requestsmock.post(
        buildhub.SEARCH_URL,
        json={
            "aggregations": {
                "myaggs": {
                    "target.version": {"buckets": [{"key": "64.2"}, {"key": "65.1"}]}
                }
            }
        },
    )
    versions = buildhub.get_distinct_versions()
    assert versions == ["65.1", "64.2"]


def test_get_distinct_versions_majors(requestsmock):
    requestsmock.post(
        buildhub.SEARCH_URL,
        json={
            "aggregations": {
                "myaggs": {"target.version": {"buckets": [{"key": "65.1"}]}}
            }
        },
    )
    versions = buildhub.get_distinct_versions(major="65")
    assert versions == ["65.1"]


def test_get_distinct_buildids(requestsmock):
    requestsmock.post(
        buildhub.SEARCH_URL,
        json={
            "aggregations": {
                "myaggs": {
                    "build.id": {
                        "buckets": [
                            {"key": "20181130102244"},
                            {"key": "20181029104433"},
                            {"key": "20181029104433"},
                        ]
                    }
                }
            }
        },
    )
    versions = buildhub.get_distinct_buildids()
    assert versions == ["20181130102244", "20181029104433"]


def test_get_distinct_buildids_startswith(requestsmock):
    requestsmock.post(
        buildhub.SEARCH_URL,
        json={
            "aggregations": {
                "myaggs": {"build.id": {"buckets": [{"key": "20181130102244"}]}}
            }
        },
    )
    versions = buildhub.get_distinct_buildids(startswith="201811")
    assert versions == ["20181130102244"]
