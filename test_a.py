import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize('a,b', [(1, 2), (10, 11), (3, 4)])
def test_answer(a, b):
    assert func(a) == b


@pytest.fixture()
def login():
    print("登录操作")
    username = "chenlei"
    return username


class TestDemo:
    def test_a(self, login):
        print(f"a  username = {login}")

    def test_b(self):
        print("b")

    def test_c(self, login):
        print(f"c username = {login}")


if __name__ == '__main__':
    pytest.main(['test_a.py'])
