#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import MySQLdb
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(user=usr, passwd=pwd, db=db_name)
    c = db.cursor()
    c.execute("""SELECT * FROM states
            WHERE states.name LIKE BINARY'N%'
            ORDER BY states.id ASC;""")
    R = c.fetchall()
    for i in R:
        print(i)
