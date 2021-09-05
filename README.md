# CRUD Template for SQLite3


In this project, I wanted to create a simple CRUD template to use for future SQLite3 projects. For this repo I simply created a database (users) in SQLite3 then seprated each operation in its own file. You can also do the same in one file, but this is better for teaching purposes. 

## Terminology

CRUD - CREATE, READ, UPDATE, DELETE
SQLite3 - A lightweight relational database which uses PostgreSQL syntax. Not A Client-Side Server, Great for Lightweight Applications.

Hope you enjoy!

## Usage

```python
import sqlite3
connection = sqlite3.connect('users.db')
cursor = connection.cursor()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Thx

Please make sure to update tests as appropriate.

## Author
[DesignIsOrion] (https://designisorion.com)
