#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) == 4:
        uname = sys.argv[1]
        passw = sys.argv[2]
        d_base = sys.argv[3]

        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=uname,
                             passwd=passw,
                             db=d_base)

        cur = db.cursor()

        cur.execute("""SELECT cities.id, cities.name, states.name FROM states,
        cities WHERE states.id=cities.state_id ORDER BY cities.id ASC""")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        db.close()
