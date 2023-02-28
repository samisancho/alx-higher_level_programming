#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sys


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session = Session()
    
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    Session.add(state)
    Session.add(city)
    Session.commit()
