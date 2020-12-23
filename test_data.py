import pytest
import yaml


class TestData:
    @pytest.mark.parametrize("a,b", [(10, 20), (10, 5), (3, 9)])
    def test_data(self, a, b):
        print(a + b)

    @pytest.mark.parametrize(("a", "b"), [(10, 20), (10, 5), (3, 9)])
    def test_data1(self, a, b):
        print(a + b)

    @pytest.mark.parametrize(["a", "b"], [(10, 20), (10, 5), (3, 9)])
    def test_data2(self, a, b):
        print(a + b)

    @pytest.mark.parametrize(["a", "b"], yaml.safe_load(open("./data.yaml")))
    def test_data3(self, a, b):
        print(a + b)
