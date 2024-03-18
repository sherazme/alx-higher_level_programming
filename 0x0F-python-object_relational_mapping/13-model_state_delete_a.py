#!/usr/bin/python3
"""
deletes all State that conatins letter a
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

    # extract states containing a
    states = session.query(State).filter(State.name.ilike('%a%')).all()

    # delete states
    for state in states:
        session.delete(state)

    session.commit()

    session.close()
