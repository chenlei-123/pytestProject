import pytest

# conftest生效就近原则，优先在当前目录下
@pytest.fixture()
def connectDB():
    print("这是 sub_demo下面的connectDB")
