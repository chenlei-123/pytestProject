import pytest
from pythoncode.caculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a, b, expect", [(3, 5, 8), (-1, -2, -3), (100, 200, 300)])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect
