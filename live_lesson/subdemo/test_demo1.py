import pytest


def test_a(connectDB):
    print("sub_demo test_a")


@pytest.fixture()
def connectDB():
    print("test_demo1下的connectDB")


class TestB:
    def test_b(self):
        print("sub demo test_b")
