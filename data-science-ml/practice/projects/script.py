import concurrent.futures
import uuid

from sqlite4 import SQLite4 as sql


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        # This example shows how easy sqlite4 handles multithread access under the hood
        db = sql("database.db")
        db.connect()
        db.create_table("test", ["foo", "bar"])

        def insert():
            db.insert(
                "test", {"foo": str(uuid.uuid4()), "bar": str(uuid.uuid4())}
            )

        futures = [executor.submit(insert) for _ in range(50)]
        concurrent.futures.wait(futures)


if __name__ == "__main__":
    main()
