"""Behaviour and input validation for std_dev_of_list."""

import pytest

from tools.std_dev_of_list import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("1,2,3",), "0.82"),
        (("2",), "0.00"),
        (("2,2,2",), "0.00"),
        ((" -1, 0, 1 ",), "0.82"),
        (("0.5,1.5",), "0.50"),
    ],
)
def test_std_dev_of_list(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("1", "2")])
def test_std_dev_of_list_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Requires exactly one argument"


@pytest.mark.parametrize("args", [("",), ("1,,2",), ("x,2",)])
def test_std_dev_of_list_rejects_unparsable_numbers(args):
    assert run(*args) == "Error: Expected comma-separated numbers"


@pytest.mark.parametrize("args", [("nan,1",), ("inf,2",)])
def test_std_dev_of_list_rejects_non_finite_numbers(args):
    assert run(*args) == "Error: Numbers must be finite"
