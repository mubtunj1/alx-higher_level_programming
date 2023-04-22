#!/usr/bin/python3
"""
Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306
You must use the cities relationship for all State objects
Your code should not be executed when imported    
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
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
