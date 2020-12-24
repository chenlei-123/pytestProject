import allure
import pytest


def test_with_no_severity_label():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_nornal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNornalSeverity(object):
    def test_inside_the_normal_severity_test_class(self):
        pass
    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_critical_severity(self):
        pass