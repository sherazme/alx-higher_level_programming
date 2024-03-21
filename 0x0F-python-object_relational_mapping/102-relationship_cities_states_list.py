#!/usr/bin/python3
'''Prints City objects and State '''
import sys
from sqlalchemy import create_engine, and_, text, tuple_
from sqlalchemy.orm import sessionmaker, relationship

from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        pword = sys.argv[2]
        db_name = sys.argv[3]
        DATABASE_URL = 'mysql://{}:{}@localhost:3306/{}'.format(
            user, pword, db_name
        )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        qu = session.query(City).join(State).order_by(City.id.asc())
        for city in qu.all():
            print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
