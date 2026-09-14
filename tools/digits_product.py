# tool: digits_product
# description: Returns the product of all digits in a number
# author: @GabrielTrifoni
# example: digits_product "123" -> "6"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    
    number = args[0]
    
    if not number:
        return "Error: Please provide a non-empty input."

    if not number.isdigit():
        return "Error: Please provide a number."

    product = 1
    for i in number:
        product *= int(i)

    return str(product)
