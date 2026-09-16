# tool: is_multiple
# description: Check whether the first integer is a multiple of the second
# author: @00200200
# example: is_multiple "10" "5" -> "True"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Requires exactly two integers"
    try:
        number, divisor = (int(value) for value in args)
    except ValueError:
        return "Error: Arguments must be integers"
    if divisor == 0:
        return "Error: Divisor must not be zero"
    return str(number % divisor == 0)
