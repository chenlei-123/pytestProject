import pytest


def add_function(a, b):
    return a + b


@pytest.mark.parametrize('a', [0, 1, 3])
@pytest.mark.parametrize('b', [2, 3, 6])
def test_foo(a, b):
    print("测试参数叠加组合：a->%s,b->%s" % (a, b))
