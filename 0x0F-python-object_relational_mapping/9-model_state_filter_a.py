#!/usr/bin/python3
"""
lists all State objects that conatins letter a from database
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create session
    session = Session()

    # extract state
    states = session.query(State).filter(State.name.ilike('%a%')) \
                    .order_by(State.id).all()

    # print states
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
