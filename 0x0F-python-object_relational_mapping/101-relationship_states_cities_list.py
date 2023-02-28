#!/usr/bin/python3

import sys
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
    query = Session.query(State).order_by(State.id)
    for el in query:
        print("{}: {}".format(el.id, el.name))
        for city in el.cities:
            print("    {}: {}".format(city.id, city.name))
