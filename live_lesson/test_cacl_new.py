import pytest
import yaml

from pythoncode.caculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def test_add(self, get_calc, get_datas):
        result = get_calc.add(get_datas[0], get_datas[1])
        assert result == get_datas[2]
