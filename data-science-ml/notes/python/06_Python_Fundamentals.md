# Python Fundamentals

## Python Calculations

In Python, we can perform basic math! Who knew?

```python
# Prints "500"
print(573 - 74 + 1)

# Prints "50"
print(25 * 2)

# Prints "2.0"
print(10 / 5)
```

## Python Variables

Python, like most languages, can store values in variables. These variables can be used in calculations and other operations.

```python
coffee_price = 1.50
number_of_coffees = 4

# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# Updating the price
coffee_price = 2.00

# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
```

## Exponents in Math

Python can also perform exponentiation. In written math, you might see an exponent as a superscript number, but typing superscript numbers isn't always easy on modern keyboards. So, we use `**` to represent an exponent.

```python
# 2 to the 10th power, or 1024
print(2 ** 10)
```

## Modulo

Python can also perform modulo, which returns the remainder from a division calculation. `10 % 3` will return `1` because `3` goes into `10` three times, with a remainder of `1`.

```python
# Prints 1
print(29 % 10)
```

## Concatenation

Python can also combine strings using the `+` operator. This is called concatenation.

```python
greeting_text = "Hey there!"
question_text = "How are you doing?"

# Combines two strings
# Prints "Hey there! How are you doing?"
print(greeting_text + " " + question_text)
```

## `+=` Operator

Python supports a `+=` operator that allows you to add to a variable. This is called the addition assignment operator.

```python
# Initializes a variable with an integer value
number_of_miles_hiked = 12

# Adds a value to the initialized variable
# Prints 17
number_of_miles_hiked += 5
print(number_of_miles_hiked)
```

## Multi-Line Strings

Python supports multi-line strings. These strings are surrounded by three quotation marks. This is useful for long strings.

```python
# Multi-line string
address_string = """136 Whowho Lane
Apt 7

Whoville
"""

# Prints multi-line string
# 136 Whowho Lane
# Apt 7
#
# Whoville
print(address_string)
```
