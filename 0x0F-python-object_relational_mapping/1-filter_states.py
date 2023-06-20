#!/usr/bin/python3
"""
    List all states and filter where name starts with N
    Ordered by state ID
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              password=sys.argv[2], db=sys.argv[3],
                              port=3306)

    cur = db_conn.cursor()
    cur.execute("""
                SELECT * FROM states WHERE name like 'N%'
                ORDER BY states.id
                """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_conn.close()