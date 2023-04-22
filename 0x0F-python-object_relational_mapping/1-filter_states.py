#!/usr/bin/env python3
"""a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states WHERE \
                        name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
    db_cursor.close()
    db_connect.close()
