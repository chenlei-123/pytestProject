import allure
import pytest


@allure.link("http://www.baidu.com", name="连接")
def test_with_link():
    print("这是一个添加了连接的测试")
    pass


TEST_CASE_LINK = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=air%20pod%E5%8F%AF%E4%BB%A5%E8%BF%9E%E6%8E%A5Macbook%E5%90%97&fenlei=256&rsv_pq=eef316380002ff23&rsv_t=8f51zZhu8FkPmFB4VXeA3fSU8cR4VMwEt8EbkgsqojsfLY%2BZMjPPANCreOk&rqlang=cn&rsv_enter=1&rsv_dl=ib&rsv_sug2=0&rsv_btype=i&inputT=14421&rsv_sug4=14421'
@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接，链接到测试用例里面")
    pass

# --allure-link-pattern=issue:http://www.mytesttracker.com/issue{}
@allure.issue('140','这是一个issue')
def test_with_issue_link():
    pass
