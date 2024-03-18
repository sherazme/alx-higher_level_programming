#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make connection with database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    qu = """SELECT c.name FROM cities c
          INNER JOIN states s ON s.id = c.state_id
          WHERE s.name = %s ORDER BY c.id ASC"""
    cur.execute(qu, [argv[4]])

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Close process
    cur.close()
    db.close()
