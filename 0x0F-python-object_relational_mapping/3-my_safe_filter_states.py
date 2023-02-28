#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) == 5:
        usrnm = sys.argv[1]
        passw = sys.argv[2]
        d_base = sys.argv[3]
        name = sys.argv[4]

        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=usrnm,
                             passwd=passw,
                             db=d_base)

        cur = db.cursor()

        d_query = "SELECT * FROM states WHERE name=%s"
        cur.execute(d_query, (name,))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
