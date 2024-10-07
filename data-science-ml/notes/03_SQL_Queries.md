# SQL Queries

This module builds off of the basics and foundations from the first module where we learned the basics of creating tables, adding records, dropping records, and modifying records.

## `AS` Keyword

The `AS` keyword is used to rename a column or table with an alias. This is useful when you want to rename a column or table in a query. For example:

```sql
SELECT name AS 'Titles'
FROM movies;
```

This query renames the `name` column to `Titles` when the query is returned. Note that this does not alter the original table.

## `DISTINCT` Keyword

The `DISTINCT` keyword is used to return only distinct (different) values. For example:

```sql
SELECT DISTINCT genre
FROM movies;
```

This query returns only the distinct genres from the `movies` table.

## `WHERE` Clause

The `WHERE` clause is used to filter records. The `WHERE` clause is used to extract only the records that fulfill a specified condition. For example:

```sql
SELECT *
FROM movies
WHERE imdb_rating < 5;
```

## `LIKE` Operator

The `LIKE` operator is used in a `WHERE` clause to search for a specified pattern in a column. `LIKE` is For example:

```sql
SELECT *
FROM movies
WHERE name LIKE 'Se_en';
```

This query selects all records where the `name` column has a value that starts with `Se`, ends with `en`, and has exactly one character in between. The `_` is a wildcard character that matches any single character.

### Regular Expression Wildcards

In the above example, we used `_` to pattern match a single character with a wildcard. We can also use `%` to match any sequence of characters. For example:

```sql
SELECT *
FROM movies
WHERE name LIKE 'A%';
```

This query selects all records where the `name` column starts with the letter `A`. What if we wanted to select all records where the `name` column ends with the letter `a`? We could use:

```sql
SELECT *
FROM movies
WHERE name LIKE '%a';
```

One step further: what if we wanted to select all records where the `name` column contains the word `man` anywhere in the column? We could use:

```sql
SELECT *
FROM movies
WHERE name LIKE '%man%';
```

## `NULL` Values

A field with a `NULL` value is a field with no value. It is very important to understand that a `NULL` value is different from a zero value or a field that contains spaces. A field with a `NULL` value is one that has been left blank during record creation. For example:

```sql
SELECT *
FROM movies
WHERE imdb_rating IS NULL;
```

This query selects all records where the `imdb_rating` column has a `NULL` value.

## `BETWEEN` Operator

The `BETWEEN` operator selects values within a given range. The values can be numbers, text, or dates. For example:

```sql
SELECT *
FROM movies
WHERE imdb_rating BETWEEN 7 AND 9;
```

This query selects all records where the `imdb_rating` column has a value between 7 and 9.

When dealing with text values, the `BETWEEN` operator is case-sensitive and searches for values alphabetically. For example:

```sql
SELECT *
FROM movies
WHERE name BETWEEN 'A' AND 'J';
```

Note that the starting value is inclusive and the ending value is exclusive. That means this query will select all records where the `name` column has a value that starts with `A` and will do that same for all values up to and including `I`. Some odd behavior here: if we had a movie that was named 'J', our query would return that record as well. This is because `BETWEEN` _goes up to_ the second value.

## `AND` Operator

We've seen the `AND` operator in the `BETWEEN` operator example above. The `AND` operator is used to filter records based on more than one condition. The `AND` operator displays a record if all the conditions separated by `AND` are `TRUE`. For example:

```sql
SELECT *
FROM movies
WHERE imdb_rating > 7
    AND genre = 'Action';
```

This query selects all records where the `imdb_rating` column has a value greater than 7 and the `genre` column has a value of `Action`.

Another example:

```sql
SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979
    AND imdb_rating > 8;
```

We could write SQL all on one line, but just like we separate lines with returns to make our code more readable, we can do the same with indentation.

## `OR` Operator

Like the `AND` operator, `OR` allows us to combine multiple conditions. The difference with `OR` is that this operator will return a record if _any_ of the conditions we've set return true.

```sql
SELECT *
FROM movies
WHERE year > 2014
   OR genre = 'action';
```

## `ORDER BY` Clause

The `ORDER BY` clause is used to sort the result-set in ascending or descending order. The `ORDER BY` clause sorts the records in ascending order by default. To sort the records in descending order, you can use the `DESC` keyword. For example:

```sql
SELECT *
FROM movies
ORDER BY name;
```

or:

```sql
SELECT *
FROM movies
ORDER BY name DESC;
```

`ORDER BY` is always used after `WHERE` when `WHERE` is used. If you don't use `WHERE`, you can use `ORDER BY` at the end of your query.

## `LIMIT` Clause

The `LIMIT` clause is used to specify the number of records to return. The `LIMIT` clause is used in the `SELECT` statement and is helpful when working with large datasets. We may want to only return a few records to get a sense of the data. For example:

```sql
SELECT *
FROM movies
LIMIT 5;
```

`LIMIT` is always used at the end of the query and is not available in all SQL databases (since we are working in SQLite, we have this clause available).

```sql
select *
from movies
order by imdb_rating desc
limit 3;
```

## `CASE` Statement

`CASE` statements are SQL's way of handling if-then logic. We are typically using case in a `SELECT` statement to return outputs under different conditions.

```sql
SELECT name,
    CASE
        WHEN imdb_rating > 8 THEN 'Fantastic'
        WHEN imdb_rating > 6 THEN 'Poorly Received'
        ELSE 'Avoid at All Costs'
    END AS 'Review'
FROM movies;
```

Note that in the above statement, we can also use an alias to return the result with a human-readable name.

Here's a fun little error:

```sql
SELECT name
    CASE
        WHEN genre = 'romance' or genre = 'comedy' THEN 'Chill'
        ELSE 'Intense'
    END AS 'Mood'
FROM movies;
```

The above doesn't work because we forgot a comma after `name`. This is a common error when writing SQL queries.

Fixed:

```sql
SELECT name,
    CASE
        WHEN genre = 'romance' or genre = 'comedy' THEN 'Chill'
        ELSE 'Intense'
    END AS 'Mood'
FROM movies;
```
