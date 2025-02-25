import pytest
import time
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

    @pytest.mark.slow
    def test_very_slow(self):
        time.sleep(5)
        result = my_functions.divide(10, 5)
        assert result == 2

    @pytest.mark.skip(reason="This feature is currently broken")
    def test_add(self):
        time.sleep(5)
        assert my_functions.add(1, 2) == 3
        
    @pytest.mark.xfail(reason="We kmow we can't divide by zero")
    def test_divide_zero_broken():
        my_functions.divide(4,0)