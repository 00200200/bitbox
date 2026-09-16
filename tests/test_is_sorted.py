"""Behaviour and input validation for is_sorted."""

import pytest

from tools.is_sorted import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("1,2,3,4",), "True"),
        (("1,1,2",), "True"),
        (("1,3,2",), "False"),
        (("9",), "True"),
        (("-3,-2,0",), "True"),
        (("0.11,0.2",), "True"),
        (("9007199254740993,9007199254740992",), "False"),
    ],
)
def test_is_sorted(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("1", "2")])
def test_is_sorted_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Requires exactly one argument"


@pytest.mark.parametrize("args", [("",), ("1,,2",), ("x,2",)])
def test_is_sorted_rejects_unparsable_numbers(args):
    assert run(*args) == "Error: Expected comma-separated numbers"


@pytest.mark.parametrize("args", [("nan,1",), ("inf,2",)])
def test_is_sorted_rejects_non_finite_numbers(args):
    assert run(*args) == "Error: Numbers must be finite"
