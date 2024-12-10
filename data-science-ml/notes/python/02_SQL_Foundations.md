# SQL Foundations

Querying data from a database is fundamental for data science and data analytics because, when working with a well-cleaned and well-established dataset, data is typically stored in a relational database.

This module covers:
- Manipulating data
- Querying data
- Aggregating data
- Working with multiple tables
- Data acquisition

## Exploring Data with SQL

Structured Query Language (SQL) is a language that allows us to write queries to access data within a database based on a set of rules and requirements.

For example:
```sql
SELECT *
FROM table
LIMIT 10;
```

## Relational Databases

A relational database is a type of database. A relational database structures data in such a way that allows us to identify and access data in relation to another piece of data in the database. The data is typically organized in tables.

In tables, we have rows and columns. Each row is called a record. Columns are labeled with a descriptive name and have a specific data type. A single column will not have mixed data types.

## Relational Database Management Systems

Some of the more popular database systems are: MySQL, PostgreSQL, Oracle DB, SQL Server, and SQLite.

## SQL Language

Syntax examples in SQL:

### Basic Query

The most basic selection of all content from a table:

```sql
select * from table
```

### Creating a Table and Statements

```sql
create table table_name (
    column_1 data_type,
    column_2 data_type,
    coulmn_3 data_type
);
```

```sql
create table celebs (
    id      integer,
    name    text,
    age     integer
);
```

### Inserting Data into a Table

Once we have a table created, we need to add data to it:

```sql
insert into celebs (id, name, age)
values (1, 'Justin Bieber', 29);
```

`insert into` is a caluse that adds the specified row or rows, `celebs` is the table, `(id, name, age)` are the parameters identifying the columns that data will be inserted into.

`values` is another clause that indicates the data being inserted and `(1, 'Justin Bieber', 29)` is a parameter identifying the values being inserted.

### Manipulating Data

We can fetch data with a `select` statement. For example:

```sql
select name from celebs;
```

### Altering Records

We can also add table records after creating the table using the `alter table` statement.

```sql
alter table celebs
add column twiter_handle text;
```

This is where things get intersting. Since our table did not previously include a column `twitter_handle`, all previously entered records now gain a `null` value.

### `update` Statement

The `update` statement allows us to edit rows in a table. We use it when we want to change *existing* records.

```sql
update celebs
set twitter_handle = '@taylorswift13'
where id = 4;
```

This is sdifferent from the `alter` statement, which is used to modify columns. Using `alter` we can add, remove or modify a column. Update can only modify, not remove or add.

### Deleting Records

We can also delete records from our table with `delete`. Using the statement `delete from` and funneling with `where` allows us to remove records that match certain criteria.

```sql
delete from celebs
where twitter_handle is null;
```

This statement drops all records that have a `null` twitter_handle value.

### Constraints

Upon creating a table, it's important that we set constraints that require the database records to adhere to certain conditions.

```sql
CREATE TABLE celebs (
   id INTEGER PRIMARY KEY,
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);
```

`primary key` is a built in record tool that assigns a unique identifier to our record on creation.

## Example SQL

```sql
CREATE TABLE friends(
  id        INTEGER,
  name      TEXT,
  birthday  DATE
);

INSERT INTO friends(id, name, birthday)
values (1, 'Ororo Munroe', 'May 30th, 1940');

SELECT *
FROM friends;

INSERT INTO friends(id, name, birthday)
values (2, 'Bob Stevens', 'May 30th, 1940');
INSERT INTO friends(id, name, birthday)
values (3, 'Rob Boberson', 'May 30th, 1940');

UPDATE friends
set name = 'Storm'
WHERE id = 1;

SELECT *
FROM friends;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
set email = 'storm@codeacademy.com'
where id = 1;

SELECT *
FROM friends;

DELETE FROM friends
where name = 'Storm';

SELECT *
FROM FRIENDS;
```














