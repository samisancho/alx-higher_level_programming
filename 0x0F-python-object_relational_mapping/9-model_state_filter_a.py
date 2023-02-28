#!/usr/bin/python3
""" List the first match from a query usng sqlalvchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import(create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    """st = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(st.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]), pool_pre_ping=True)"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session = Session()

    query = Session.query(State).order_by(State.id)
    query = query.filter(State.name.like('%a%'))

    for el in query:
        print("{}: {}".format(el.id, el.name))
