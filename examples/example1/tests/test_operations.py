import pytest

from math_calcs import (
    add,
    subtract,
    multiply,
    divide,
    power,
    factorial,
    fibonacci,
    is_prime,
    gcd,
    lcm,
    mean,
    median,
)


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_mixed_signs(self):
        assert add(-3, 7) == 4

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_positive_result(self):
        assert subtract(10, 3) == 7

    def test_negative_result(self):
        assert subtract(3, 10) == -7

    def test_floats(self):
        assert subtract(5.5, 2.2) == pytest.approx(3.3)

    def test_zero(self):
        assert subtract(5, 0) == 5


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(4, 5) == 20

    def test_by_zero(self):
        assert multiply(100, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-3, -4) == 12

    def test_mixed_signs(self):
        assert multiply(-3, 4) == -12

    def test_floats(self):
        assert multiply(2.5, 4) == 10.0


class TestDivide:
    def test_even_division(self):
        assert divide(10, 2) == 5.0

    def test_fractional_result(self):
        assert divide(7, 2) == 3.5

    def test_negative_division(self):
        assert divide(-10, 2) == -5.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_float_division(self):
        assert divide(1.0, 3.0) == pytest.approx(0.3333333333)


class TestPower:
    def test_square(self):
        assert power(3, 2) == 9

    def test_cube(self):
        assert power(2, 3) == 8

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == 0.5

    def test_fractional_exponent(self):
        assert power(9, 0.5) == pytest.approx(3.0)


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_small_number(self):
        assert factorial(5) == 120

    def test_larger_number(self):
        assert factorial(10) == 3628800

    def test_negative_raises(self):
        with pytest.raises(ValueError, match="not defined for negative"):
            factorial(-1)


class TestFibonacci:
    def test_zero(self):
        assert fibonacci(0) == 0

    def test_one(self):
        assert fibonacci(1) == 1

    def test_small_index(self):
        assert fibonacci(6) == 8

    def test_tenth(self):
        assert fibonacci(10) == 55

    def test_negative_raises(self):
        with pytest.raises(ValueError, match="not defined for negative"):
            fibonacci(-1)


class TestIsPrime:
    def test_zero_not_prime(self):
        assert is_prime(0) is False

    def test_one_not_prime(self):
        assert is_prime(1) is False

    def test_two_is_prime(self):
        assert is_prime(2) is True

    def test_three_is_prime(self):
        assert is_prime(3) is True

    def test_four_not_prime(self):
        assert is_prime(4) is False

    def test_large_prime(self):
        assert is_prime(97) is True

    def test_large_composite(self):
        assert is_prime(100) is False

    def test_negative_not_prime(self):
        assert is_prime(-7) is False


class TestGcd:
    def test_common_case(self):
        assert gcd(12, 8) == 4

    def test_coprime(self):
        assert gcd(7, 13) == 1

    def test_same_number(self):
        assert gcd(5, 5) == 5

    def test_one_is_zero(self):
        assert gcd(0, 9) == 9


class TestLcm:
    def test_common_case(self):
        assert lcm(4, 6) == 12

    def test_coprime(self):
        assert lcm(3, 7) == 21

    def test_same_number(self):
        assert lcm(5, 5) == 5

    def test_one_is_one(self):
        assert lcm(1, 8) == 8


class TestMean:
    def test_integers(self):
        assert mean([1, 2, 3, 4, 5]) == 3.0

    def test_single_value(self):
        assert mean([42]) == 42.0

    def test_floats(self):
        assert mean([1.5, 2.5, 3.0]) == pytest.approx(2.3333333333)

    def test_empty_raises(self):
        with pytest.raises(ValueError, match="empty list"):
            mean([])


class TestMedian:
    def test_odd_count(self):
        assert median([3, 1, 2]) == 2

    def test_even_count(self):
        assert median([1, 2, 3, 4]) == 2.5

    def test_single_value(self):
        assert median([7]) == 7

    def test_already_sorted(self):
        assert median([10, 20, 30, 40, 50]) == 30

    def test_empty_raises(self):
        with pytest.raises(ValueError, match="empty list"):
            median([])
