from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# import sqlalchemy
import sqlite3


def task_1(path):
    conn = sqlite3.connect(path)
    curs = conn.cursor()
    curs.execute("UPDATE Items SET price = price + 100 WHERE name LIKE 'b%' OR name LIKE '%e'")
    conn.commit()
    pass


class Task3(object):
    def __init__(self, path):
        self.path = path
        pass


p = 'sqlite:///base.db'
# task_1(p)

# print("Версия SQLAlchemy:", sqlalchemy.__version__)
eng = create_engine(p, echo=False)

metadata = MetaData()
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('fullname', String),
                    Column('password', String))

metadata.create_all(eng)






