# SQL Aggregate Functions

## Introduction

This lesson covers SQL aggregate functions. Aggregate functions help us perform actions on the data we query. We can use aggregate functions to count, sum, average, and find the minimum and maximum values in a column.

```sql
COUNT()
SUM()
MAX()
MIN()
AVG()
ROUND()
```

## `COUNT()`

This operand lets us perform a count of the number of records returned in a select statement.

```sql
select count(*)
from fake_apps;
```

## `SUM()`

We can use the sum operand on numerical columns and records to return the sum.

## `MAX()` and `MIN()`

These are fairly self-explanitory as well; return the minimum and maximum values.

## Chaining Operands

```sql
SELECT ROUND(AVG(price), 2)
FROM fake_apps;
```

The above will return the average of the price column rounded to two decimal places.

## `GROUP BY` and Aggregations

Instead of having to write something like this:

```sql
SELECT AVG(imdb_rating)
FROM movies
WHERE year = 1999;

SELECT AVG(imdb_rating)
FROM movies
WHERE year = 2000;

SELECT AVG(imdb_rating)
FROM movies
WHERE year = 2001;
```

We can use `GROUP BY` to return information in a single step, much more clearly:

```sql
SELECT year,
   AVG(imdb_rating)
FROM movies
GROUP BY year
ORDER BY year;
```

### More `GROUP BY` Options

Where writing

```sql
SELECT ROUND(imdb_rating),
   COUNT(name)
FROM movies
GROUP BY ROUND(imdb_rating)
ORDER BY ROUND(imdb_rating);
```

is time consuming, writing

```sql
SELECT ROUND(imdb_rating),
   COUNT(name)
FROM movies
GROUP BY 1
ORDER BY 1;
```

is much more convenient. Each column in our select statement is assigned 1,2,3... based on the order in which it appears in our select statement.

## `HAVING`

We use `HAVING` when we want to filter groups and not records.

```sql
SELECT year,
   genre,
   COUNT(name)
FROM movies
GROUP BY 1, 2
HAVING COUNT(name) > 10;
```

In the above example, we are grouping by year and genre, but filtering even further using `HAVING` to only return those years and genres in which more than 10 records.
