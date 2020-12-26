from time import sleep

import pytest


def test_rerun():
    sleep(0.5)
    assert 1 == 1


def test_rerun1():
    sleep(0.5)
    assert 1 == 1


@pytest.mark.flaky(reruns=5)
def test_rerun2():
    sleep(0.5)
    assert 1 == 2
