# tool: median_of_list
# description: Median of comma-separated numbers
# author: @00200200
# example: median_of_list "3,1,2" -> "2"

from decimal import Decimal, InvalidOperation
from statistics import median


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Requires exactly one argument"
    try:
        numbers = [Decimal(value.strip()) for value in args[0].split(",")]
    except InvalidOperation:
        return "Error: Expected comma-separated numbers"
    if not all(value.is_finite() for value in numbers):
        return "Error: Numbers must be finite"
    result = median(numbers)
    if result == result.to_integral_value():
        return str(int(result))
    return format(result, "f").rstrip("0").rstrip(".")
