#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) == 5:
        uname = sys.argv[1]
        passw = sys.argv[2]
        d_base = sys.argv[3]
        s_name = sys.argv[4]

        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=uname,
                             passwd=passw,
                             db=d_base)

        cur = db.cursor()
        d_query = """SELECT cities.name FROM cities,
        states WHERE states.name=%s AND states.id=cities.state_id"""
        cur.execute(d_query, (s_name,))

        rows = cur.fetchall()
        c, l = 0, len(rows)

        for row in rows:
            print(row[0], end=', ') if (c < l - 1) else print(row[0], end='')
            c += 1
        print()

        cur.close()
        db.close()
