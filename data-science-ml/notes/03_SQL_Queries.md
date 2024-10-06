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
