import pytest


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test_three():
    print("test_three")


class TestClass():
    def setup_method(self):
        print("\nsetup_method:   sss")

    def teardown_method(self):
        print("\nteardown_method:  ttt")

    def setup_class(self):
        print("\nsetup_class: sss")

    def teardown_class(self):
        print("\nteardown_class : tttt")

    def setup_module(self):
        print("\nsetup_module sss")

    def teardown_module(self):
        print("\nteardown_module yttt")

    def test_one(self):
        print("正在执行test one")

    def test_two(self):
        print("正在执行te¬t two")
