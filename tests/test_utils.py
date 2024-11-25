from src.utils import ip_reachable


def test_ip_reachable():
    assert ip_reachable('8.8.8.8')
