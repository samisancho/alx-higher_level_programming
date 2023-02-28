#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

if __name__ == '__main__':

    s_name = 'New Mexico'
    """st = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(st.format(sys.argv[1],
                                     sys.argv[2],
                                     sys.argv[3]),
                                     pool_pre_ping=True)"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session = Session()

    query = Session.query(State).filter_by(id=2)
    query.update({State.name: s_name}, synchronize_session=False)
    Session.commit()
