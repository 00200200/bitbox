# tool: second_largest
# description: Second-largest distinct value in comma-separated numbers
# author: @00200200
# example: second_largest "3,1,4,1,5" -> "4"

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
    distinct = sorted(set(numbers))
    if len(distinct) < 2:
        return "Error: Requires at least two distinct numbers"
    result = distinct[-2]
    if result == result.to_integral_value():
        return str(int(result))
    return format(result, "f").rstrip("0").rstrip(".")
