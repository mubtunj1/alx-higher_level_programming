#!/usr/bin/python3
"""
Write a script that lists all State objects, and
corresponding City objects, contained in the database hbtn_0e_101_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City)
    .filter(State.id == City.state_id).order_by(State.id, City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
