# Pandas Introduction and Data Analytics

Pandas is one of the most popular libraries for data analysis
and this section of the course will cover the basics of the
library.

## Lambda Functions

Lambda functions are anonymous functions, like arrow functions
in JavaScript. They allow us to name and call a function in a
single line.

```python
add_two = lambda x: x + 2

print(add_two(3)) # 5
print(add_two(5)) # 7
print(add_two(7)) # 9
```

We can also use lambda functions to perform logic:

```python
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'
```
