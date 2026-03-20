import sqlite3
import os
import time
import random

DB_FOLDER = "databases"


def print_table(cursor, rows):
    cols = [i[0] for i in cursor.description]

    widths = []
    for i, col in enumerate(cols):
        max_len = len(col)
        for r in rows:
            max_len = max(max_len, len(str(r[i])))
        widths.append(max_len)

    line = "+"
    for w in widths:
        line += "-" * (w + 2) + "+"

    print(line)

    header = "|"
    for i, col in enumerate(cols):
        header += " " + col.ljust(widths[i]) + " |"
    print(header)

    print(line)

    for r in rows:
        row = "|"
        for i, v in enumerate(r):
            row += " " + str(v).ljust(widths[i]) + " |"
        print(row)

    print(line)


def main():

    if not os.path.exists(DB_FOLDER):
        os.mkdir(DB_FOLDER)

    conn = None
    cursor = None
    current_db = None

    connection_id = random.randint(1, 100)

    print()
    print("Welcome to the LiteSQL. Commands end with ;.")
    print(f"Your SQLite connection id is {connection_id}")
    print(f"Server version: {sqlite3.sqlite_version} SQLite")
    print()
    print("Copyright (c) 2000-2026 LiteSQL contributors.")
    print("This Project is made based on SQLite ")
    print()
    
    print()

    while True:

        query = input("LiteSQL> ").strip()
        

        query = query[:-1]
        start = time.time()

        # SHOW DATABASES
        if query.lower().startswith("show databases"):

            dbs = os.listdir(DB_FOLDER)

            print("+--------------------+")
            print("| Database           |")
            print("+--------------------+")

            for db in dbs:
                if db.endswith(".db"):
                    print("|", db.replace(".db", "").ljust(18), "|")

            print("+--------------------+")
            continue

        # CREATE DATABASE
        if query.lower().startswith("create database"):

            dbname = query.split()[2]
            path = os.path.join(DB_FOLDER, dbname + ".db")

            if os.path.exists(path):
                print(f"ERROR: database '{dbname}' already exists")
                continue

            sqlite3.connect(path)

            elapsed = time.time() - start
            print(f"Query OK, 0 rows affected ({elapsed:.2f} sec)")
            continue

        # USE DATABASE
        if query.lower().startswith("use "):

            dbname = query.split()[1]
            path = os.path.join(DB_FOLDER, dbname + ".db")

            if not os.path.exists(path):
                print(f"ERROR 1049 (42000): Unknown database '{dbname}'")
                continue

            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            current_db = dbname

            print("Database changed")
            continue

        if cursor is None:
            print("No database selected")
            continue

        try:

            cursor.execute(query)

            if query.lower().startswith(("select", "show")):

                rows = cursor.fetchall()

                if rows:
                    print_table(cursor, rows)
                else:
                    print("Empty set")

                elapsed = time.time() - start
                print(f"{len(rows)} rows in set ({elapsed:.2f} sec)")

            else:

                conn.commit()

                elapsed = time.time() - start
                print(f"Query OK, {cursor.rowcount} rows affected ({elapsed:.2f} sec)")

        except Exception as e:
            print("Error:", e)

    if conn:
        conn.close()


if __name__ == "__main__":
    main()()