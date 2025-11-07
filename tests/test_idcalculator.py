import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from IDCalculator import IDCalculator


def test_calculate_8_digits():
    assert IDCalculator().calculate("12345678") == 2


def test_calculate_9_digits_strips_last():
    assert IDCalculator().calculate("123456782") == 2


def test_integer_input():
    assert IDCalculator().calculate(12345678) == 2


def test_leading_zeros():
    # example: '01234567' should still compute without losing leading zero
    assert isinstance(IDCalculator().calculate("01234567"), int)


def test_invalid_non_digits():
    with pytest.raises(TypeError):
        IDCalculator().calculate("12A45678")


def test_invalid_length():
    with pytest.raises(TypeError):
        IDCalculator().calculate("12345")
