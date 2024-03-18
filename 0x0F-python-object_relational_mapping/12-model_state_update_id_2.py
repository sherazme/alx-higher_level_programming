#!/usr/bin/python3
"""
change the name of State object in database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create Session class
    Session = sessionmaker(bind=engine)
    # create Session
    session = Session()
    Base.metadata.create_all(engine)
    state_update = session.query(State).filter_by(id='2').first()
    state_update.name = "New Mexico"

    session.commit()
    session.close()
