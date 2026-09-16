# tool: std_dev_of_list
# description: Population standard deviation of comma-separated numbers (two decimals)
# author: @00200200
# example: std_dev_of_list "1,2,3" -> "0.82"

import math
import statistics


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Requires exactly one argument"
    try:
        numbers = [float(value.strip()) for value in args[0].split(",")]
    except ValueError:
        return "Error: Expected comma-separated numbers"
    if not all(math.isfinite(value) for value in numbers):
        return "Error: Numbers must be finite"
    return f"{statistics.pstdev(numbers):.2f}"
