import pytest
from calculator import add, subtract, multiply, divide
 
class TestAdd:
    def test_positive(self):
        assert add(2, 3) == 5
 
    def test_negative(self):
        assert add(-1, 1) == 0
 
    def test_zeros(self):
        assert add(0, 0) == 0
 
class TestSubtract:
    def test_basic(self):
        assert subtract(10, 4) == 6
 
class TestMultiply:
    def test_basic(self):
        assert multiply(3, 4) == 12
 
class TestDivide:
    def test_basic(self):
        assert divide(10, 2) == 5.0
 
    def test_zero_division(self):
        with pytest.raises(ValueError):
            divide(5, 0)
