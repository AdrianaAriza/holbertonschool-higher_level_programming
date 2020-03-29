#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import MySQLdb
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    s_name = sys.argv[4]
    db = MySQLdb.connect(user=usr, passwd=pwd, db=db_name)
    c = db.cursor()
    c.execute("""SELECT cities.name
    FROM cities
    JOIN states ON states.id=cities.state_id
    WHERE states.name LIKE BINARY "{:s}"
    ORDER BY cities.id ASC""".format(s_name))
    R = c.fetchall()
    x = []
    for city in R:
        x.append(city[0])
    print(", ".join(x))
