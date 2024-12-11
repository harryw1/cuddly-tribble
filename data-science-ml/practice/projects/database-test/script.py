"""SQLite database operations example script."""

import sqlite3 as sql
import uuid


def main():
    """Open a connection to a SQLite database, create a table, insert a row, and select all rows."""
    conn = sql.connect("test.db")
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS test (id TEXT PRIMARY KEY, data TEXT)")
    conn.commit()

    c.execute(
        "INSERT INTO test (id, data) VALUES (?, ?)",
        (str(uuid.uuid4()), "Hello, World!"),
    )
    conn.commit()

    result = c.execute("SELECT * FROM test").fetchall()
    print(result)

    conn.close()


if __name__ == "__main__":
    main()
