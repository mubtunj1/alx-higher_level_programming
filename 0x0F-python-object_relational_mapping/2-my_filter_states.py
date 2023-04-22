#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db_connect = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
    db_cursor.close()
    db_connect.close()
