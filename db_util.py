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

def insert_single(table, values, db_name = "test.db"):
    """ Adds a single entry to the database.
    
    Arguments:
    - `table`: The table you want to add to.
    - `values`: A list of values to be added, e.g.:
                ["Andy", "Bromberg"]
    - `db_name`: The name of the database.
    """
    conn = sqlite3.connect(db_name)
    values.insert(0, None) # adds NULL val to list so primary key increments
    q_marks = "("+ ",".join("?" for _ in range(len(values)))  + ")"
    insert_single_cmd = "insert into " + table + " values " + q_marks
    conn.execute(insert_single_cmd, values)
    conn.commit()
    conn.close()

def get_table_contents(table, db_name = "test.db"):
    """ Returns the entire contents of a table in a list of lists, with 
        individual lists representing the rows.
    
    Arguments:
    - `table`: The table to be queried.
    - `db_name`: The name of the database.
    """
    conn = sqlite3.connect(db_name)
    get_contents_cmd = "SELECT * FROM " + table
    contents = [row for row in conn.execute(get_contents_cmd)]
    conn.close()
    return contents
    

if __name__ == '__main__':
    # build_db()
    # insert_single('author', ['Andy', 'Bromberg'])
    # insert_single('author', ['Jackson', 'Poulos'])
    # print get_table_contents('author')
    pass
