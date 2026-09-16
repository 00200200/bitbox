"""Behaviour and input validation for is_twin_prime."""

import pytest

from tools.is_twin_prime import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("3",), "True"),
        (("5",), "True"),
        (("17",), "True"),
        (("2",), "False"),
        (("7",), "False"),
        (("9",), "False"),
        (("0",), "False"),
        (("-3",), "False"),
        (("49",), "False"),
    ],
)
def test_is_twin_prime(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("3", "5")])
def test_is_twin_prime_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Requires exactly one argument"


@pytest.mark.parametrize("args", [("abc",), ("3.5",)])
def test_is_twin_prime_rejects_non_integer_argument(args):
    assert run(*args) == "Error: Argument must be an integer"
