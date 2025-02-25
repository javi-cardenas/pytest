import pytest
import src.my_functions as my_functions

class TestMyFunctions():
    def test_add(self):
        result = my_functions.add(1, 4)
        assert result == 5

    def test_add_strings(self):
        result = my_functions.add("i like ", "burgers")
        assert result == "i like burgers"

    def test_divide(self):
        result = my_functions.divide(10, 5)
        assert result == 2

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            my_functions.divide(10, 0)