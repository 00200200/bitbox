# tool: is_sorted
# description: Check whether comma-separated numbers are in nondecreasing order
# author: @00200200
# example: is_sorted "1,2,3,4" -> "True"

from decimal import Decimal, InvalidOperation


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Requires exactly one argument"
    try:
        numbers = [Decimal(value.strip()) for value in args[0].split(",")]
    except InvalidOperation:
        return "Error: Expected comma-separated numbers"
    if not all(value.is_finite() for value in numbers):
        return "Error: Numbers must be finite"
    return str(all(left <= right for left, right in zip(numbers, numbers[1:])))
