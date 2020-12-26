import pytest

from pythoncode.caculator import Calculator
import os
import yaml


@pytest.fixture()  # 默认是method级别
# @pytest.fixture(scope="class")    #类级别
# @pytest.fixture(scope="session")  #好几个文件一起执行
# @pytest.fixture(scope="module")  # module级别
def connectDB():
    print("链接数据库")
    yield
    print("断开数据库链接")


# 创建了一个登录的fixture方法
# @pytest.fixture(autouse=True)     可以直接默认调用fixture，不推荐加
@pytest.fixture()
def login():
    print("\n登陆操作")  # 相当于setup
    print("获取token")
    username = "tom"
    password = "123456"
    token = "token123456"
    yield [username, password, token]  # 相当于teardown
    print("\n登出操作")


@pytest.fixture()
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


yaml_file_path = os.path.dirname(__file__) + "/data1.yaml"

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    print(datas)
    add_datas = datas["datas"]
    add_ids = datas["myids"]


@pytest.fixture(params=add_datas, ids=add_ids)
def get_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")
