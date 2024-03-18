#!/usr/bin/python3
"""
list of all State objects from the database
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create Session class
    Session = sessionmaker(bind=engine)
    # create Session
    session = Session()
    Base.metadata.create_all(engine)

    s_tate = session.query(State).order_by(State.id).all()
    for state in s_tate:
        print("{}: {}".format(state.id, state.name))
    session.close()
