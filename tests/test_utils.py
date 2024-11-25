import pytest

from src import utils


@pytest.fixture
def monkeypatch():
    yield


def test_ip_reachable(monkeypatch):
    host = 'example.com'
    result = utils.ip_reachable(host)
    assert result is True  # or any other expected behavior
