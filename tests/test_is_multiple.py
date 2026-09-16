"""Behaviour and input validation for is_multiple."""

import pytest

from tools.is_multiple import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("10", "5"), "True"),
        (("11", "5"), "False"),
        (("0", "5"), "True"),
        (("-10", "5"), "True"),
        (("10", "-5"), "True"),
        (("9007199254740993", "3"), "True"),
    ],
)
def test_is_multiple(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("1",), ("1", "2", "3")])
def test_is_multiple_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Requires exactly two integers"


@pytest.mark.parametrize("args", [("x", "2"), ("1.5", "2")])
def test_is_multiple_rejects_non_integer_arguments(args):
    assert run(*args) == "Error: Arguments must be integers"


def test_is_multiple_rejects_zero_divisor():
    assert run("1", "0") == "Error: Divisor must not be zero"
