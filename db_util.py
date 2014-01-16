#!/usr/bin/env python
# -*- coding: utf-8 -*-.
"""
Contains all functions needed to interface with SQLite databases.
"""

import sqlite3

def build_db(db_name = "test.db"):
    """ Creates the database and then builds all of the individual
        tables.
    
    Arguments:
    - `db_name`: The name of the database.
    """
    conn = sqlite3.connect(db_name)
    create_tables_cmd = """
    CREATE TABLE author (id INTEGER PRIMARY KEY, first TEXT, last TEXT);
    CREATE TABLE article (id INTEGER PRIMARY KEY, title TEXT, body TEXT,
    author INTEGER, FOREIGN KEY(author) REFERENCES author(id));
    """
    conn.executescript(create_tables_cmd)
    conn.commit()
    conn.close()

def insert_single(db_name, table, values):
    """ Adds a single entry to the database.
    
    Arguments:
    - `db_name`: The name of the database.
    - `table`: The table you want to add to.
    - `values`: A list of values to be added, e.g.:
                ["Andy", "Bromberg"]
    """
    conn = sqlite3.connect(db_name)
    values.insert(0, None)
    q_marks = "("+ ",".join("?" for _ in range(len(values)))  + ")"
    insert_single_cmd = "insert into " + table + " values " + q_marks
    conn.execute(insert_single_cmd, values)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #build_db()
    #insert_single('test.db', 'author', ['Andy', 'Bromberg'])
    
