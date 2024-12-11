# Working with Multiple Tables

## Introduction

Spreading data accross tables is comming in relational database management. We find data distributed across multiple tables to avoid redundancy and to improve data integrity.

Codeacademy uses an example of a magazine subscription service to illustrate how data can be distributed across multiple tables. The database has three tables: `subscriptions`, `customers`, and `magazines`. Since a customer can have multiple subscriptions and a magazine can have multiple subscribers, the `subscriptions` table is used to keep track of the relationships between customers and magazines and reduce redundancy.

## Joining Tables

In order to work with data from multiple tables, we need to use `JOIN` clauses to combine rows from two or more tables based on a related column between them. The `JOIN` clause is used to combine rows from two or more tables based on a related column between them.

Starting with the most basic `JOIN`:

```sql
SELECT *
FROM orders
JOIN customers
  ON orders.customer_id = customers.customer_id;
```

In this example, the `JOIN` clause is used to combine rows from the `orders` and `customers` tables based on the `customer_id` column. The `ON` keyword is used to specify the condition that links the two tables together.

If we want to select specific columns from the tables, we can specify the column names in the `SELECT` statement:

```sql
SELECT orders.order_id,
   customers.customer_name
FROM orders
JOIN customers
  ON orders.customer_id = customers.customer_id;
```

Notice that we have to specify the table name when selecting columns that have the same name in both tables.

Another example:

```sql
select *
from orders
join subscriptions
  on orders.subscription_id =
    subscriptions.subscription_id;

select *
from orders
join subscriptions
  on orders.subscription_id =
    subscriptions.subscription_id
where subscriptions.description
  = 'Fashion Magazine';
```

## Types of Joins and Primary Keys

There are different types of `JOIN` clauses that can be used to combine rows from two or more tables:

- `INNER JOIN`: returns rows when there is at least one match in both tables.
- `LEFT JOIN`: returns all rows from the left table, and the matched rows from the right table.
- `RIGHT JOIN`: returns all rows from the right table, and the matched rows from the left table.
- `FULL JOIN`: returns rows when there is a match in one of the tables.

### Primary Keys

A primary key is a column that uniquely identifies each row in a table. It must contain a unique value for each row and cannot contain `NULL` values. In the example above, the `customer_id` column in the `customers` table is the primary key. A single table cannot have more than one primary key; however, a primary key can consist of multiple columns (composite key).

#### Foreign Keys

When a primary key from one table is used in another table, it is called a foreign key. In the example above, the `customer_id` column in the `orders` table is a foreign key that references the `customer_id` column in the `customers` table.

### Importance of Primary and Foreign Keys

Most common types of joins will be working with primary and foreign keys.

> For instance, when we join `orders` and `customers`, we join on `customer_id`, which is a foreign key in `orders` and the primary key in `customers`.

### `INNER JOIN`

The `INNER JOIN` clause is used to combine rows from two or more tables based on a related column between them. It returns rows when there is at least one match in both tables.

```sql
SELECT *
FROM orders
INNER JOIN customers
  ON orders.customer_id = customers.customer_id;
```

The final result will contain only the rows where the `customer_id` column in the `orders` table matches the `customer_id` column in the `customers` table.

### `LEFT JOIN`

The `LEFT JOIN` clause returns all rows from the left table, and the matched rows from the right table. The result is `NULL` from the right side, if there is no match.

```sql
SELECT *
FROM orders
LEFT JOIN customers
  ON orders.customer_id = customers.customer_id;
```

### `CROSS JOIN`

Somtimes we want to have all records from two different, unrelated tables. In this case, we can use a `CROSS JOIN` to get the Cartesian product of the two tables.

```sql
SELECT shirts.shirt_color,
   pants.pants_color
FROM shirts
CROSS JOIN pants;
```

Notice we don't have an `ON` clause in a `CROSS JOIN`, since we aren't really joining on any columns.

More cross join examples:

```sql
select count(*)
from newspaper
where start_month <= 3 and end_month >=3;

select *
from newspaper
cross join months;

select *
from newspaper
cross join months
where start_month <= month and end_month >= month;

select month,
  count(*)
from newspaper
cross join months
where start_month <= month and end_month >= month
group by month;
```

### `UNION`

This operator is used when we want to 'stack' two tables on top of each other. The tables must have the same number of columns and the same data types in the same order to be able to use `UNION`.

```sql
SELECT *
FROM table1
UNION
SELECT *
FROM table2;
```

### `WITH`

The `WITH` clause is used to define a temporary table that can be used in the `SELECT` statement. It is useful when we want to use the same subquery multiple times in a query.

```sql
WITH previous_results AS (
   SELECT ...
   ...
   ...
   ...
)
SELECT *
FROM previous_results
JOIN customers
  ON _____ = _____;
```

For example:

```sql
WITH previous_query AS (
SELECT customer_id,
       COUNT(subscription_id) AS 'subscriptions'
       FROM orders
       GROUP BY customer_id)
SELECT customers.customer_name,
    previous_query.subscriptions
FROM previous_query
JOIN customers
    ON customers.customer_id = previous_query.customer_id;
```
