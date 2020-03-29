#!/usr/bin/python3
"""Start link class to table in database
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State, City).select_from(State).join(City)
    for citie in cities:
        print("{}: ({}) {}".format(citie[0].name, citie[1].id, citie[1].name))
