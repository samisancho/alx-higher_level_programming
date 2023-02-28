#!/usr/bin/python3
"""
    Script to conect to a sql db using MySQLdb client in python
"""
import sys
import MySQLdb


if len(sys.argv) == 4:
    usrn = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
        port=3306,
        user=usrn,
        passwd=passw,
        db=db_name
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE (name REGEXP '^N')")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
