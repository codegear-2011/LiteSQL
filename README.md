

# LiteSQL

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)



LiteSQL is a lightweight, MySQL-like command-line database tool built with Python and SQLite.  
It lets you create databases, switch between them, and run SQL queries from a simple terminal interface.

## Features

- `SHOW DATABASES;` to list databases
- `CREATE DATABASE name;` to create a new database
- `USE name;` to select a database
- SQL query support through SQLite
- Table-style output for `SELECT` queries
- `help;` and `\h` for command help
- `license;` and `\l` for license text
- Works in terminal / Pydroid 3

## Requirements

- Python 3.10+
- `sqlite3` (built into Python)

No external package is required for the core database engine.

## Installation

### From source

```bash
pip install litesql
```

## Running LiteSQL

If installed:
```
litesql
```
If you want to run directly from Python:
```
python -m litesql
```


## Commands

* Database commands *

- SHOW DATABASES;
- CREATE DATABASE test;
- USE test;

 Help 

- help;
- \h

 License 

- license;
- \l

Exit 

- exit
- quit

## Example Session
```
Welcome to the LiteSQL. Commands end with ;.
Your SQLite connection id is 56
Server version: 3.48.0 SQLite

LiteSQL> CREATE DATABASE test;
Database created

LiteSQL> USE test;
Database changed

LiteSQL> CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Address VARCHAR(255),
    City VARCHAR(255)
);

LiteSQL> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| test               |
+--------------------+
```
## Notes:

- Every command must end with ;

- Database files are stored inside the databases folder
---
## License

MIT License
---
## Author

Built by Code Gear P.V.T L.T.D
---
 
