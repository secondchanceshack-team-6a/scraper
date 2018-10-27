from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__db_setup = False
__db_sessionmaker = None

def get_db_conn():
    global __db_setup
    global __db_sessionmaker
    if not __db_setup:
        __db_setup = True
        engine = create_engine('sqlite://:memory:', echo=True)
        __db_sessionmaker = sessionmaker(bind=engine)
    return __db_sessionmaker()

# new_user = User(name='ed', fullname='Ed Jones', password='edspassword')
# session.add(new_user)
