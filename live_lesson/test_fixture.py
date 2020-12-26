import pytest


# fixture是pytest的一个外壳函数，可以模拟setup,teardown操作
# yeild之前操作相当于setup，之后的操作相当于teardown
# yield相当于return，如果需要返回数据的话，直接放在yield之后


# 测试用例1，需要提前登陆，直接传递fixture名称的方式
def test_case1(login):
    print(f"login username and password:{login[0], login[1], login[2]}")
    print("\n测试用例1")


# 测试用例2，不需要提前登陆
def test_case2(connectDB):
    print("\n测试用例1")


# 测试用例3，需要提前登陆，注解的方式
@pytest.mark.usefixtures("login")
def test_case3():
    print("\n测试用例1")


# 测试用例4，不需要提前登陆
def test_case4():
    print("\n测试用例1")
