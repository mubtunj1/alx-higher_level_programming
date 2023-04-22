#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states \
                        WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
    db_cursor.close()
    db_connect.close()
