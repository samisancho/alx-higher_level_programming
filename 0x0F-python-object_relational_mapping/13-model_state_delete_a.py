#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    st = 'mysql+mysqldb://{}:{}@localhost/{}'
    """engine = create_engine(st.format(sys.argv[1],
                                     sys.argv[2],
                                     sys.argv[3]),
                                     pool_pre_ping=True)"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session = Session()

    query = Session.query(State).order_by(State.id)

    for el in query:
        if 'a' in el.name:
            Session.delete(el)
    Session.commit()
