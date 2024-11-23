add_two = lambda my_input: my_input + 2
"""
This script defines a lambda function `add_two` that takes a single input and returns the input value incremented by 2.

Functions:
    add_two(my_input): Adds 2 to the input value and returns the result.

Example:
    >>> add_two(4)
    6

<WHAT TO RETURN IF STATEMENT IS TRUE> if <IF STATEMENT> else <WHAT TO RETURN IF STATEMENT IS FALSE>
"""

print(add_two(4))

multiple_of_three = lambda num: "not a multiple" if num%3 else "multiple of three"

print(multiple_of_three(9))
print(multiple_of_three(11))