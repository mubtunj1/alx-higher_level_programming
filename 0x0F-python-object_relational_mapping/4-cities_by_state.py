#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db_connect = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT cities.id, cities.name, states.name \
                        FROM cities JOIN states ON cities.state_id \
                            = states.id ORDER BY cities.id ASC")
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
    db_cursor.close()
    db_connect.close()
