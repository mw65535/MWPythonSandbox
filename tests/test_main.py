import pytest

import calculator


class TestAdd:
    def test_positive(self):
        assert calculator.add(2, 3) == 5

    def test_negative(self):
        assert calculator.add(-1, -4) == -5

    def test_zero(self):
        assert calculator.add(0, 0) == 0


class TestSubtract:
    def test_basic(self):
        assert calculator.subtract(10, 3) == 7

    def test_result_negative(self):
        assert calculator.subtract(3, 10) == -7


class TestMultiply:
    def test_basic(self):
        assert calculator.multiply(4, 5) == 20

    def test_by_zero(self):
        assert calculator.multiply(100, 0) == 0


class TestDivide:
    def test_basic(self):
        assert calculator.divide(10, 2) == 5.0

    def test_fractional_result(self):
        assert calculator.divide(1, 3) == pytest.approx(1 / 3)

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(1, 0)
