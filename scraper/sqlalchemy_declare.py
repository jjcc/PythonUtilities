# -*- coding: UTF-8 -*-
'''
@author: jchen
@summary: 
'''
#!/usr/bin/python

import datetime
from timeit import default_timer as timer



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.schema import MetaData
from sqlalchemy import *





#########################################
# DB connection


mssql_coonect_str = "mssql+pymssql://osgg-server/NHP"

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)




#云南白药(SZ.000538),平均 69.13 买入,2016-07-07 开仓,平均 66.91 卖出,2016-07-08 平仓,25000,-3.21%,跑输大盘###

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    symbol = Column(String(20), nullable=False)
    buy_price =Column(REAL,nullable=False)
    buy_date = Column(DATETIME, nullable=False)
    sell_price = Column(REAL,nullable=False)
    sell_date = Column(DATETIME, nullable=False)
    quantity  = Column(Integer, nullable=False)
    gain_percentage = Column(REAL,nullable=False)
    win_market  = Column(BOOLEAN)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///trade.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
print "Now create sqlalchemy engin"
start = timer()

Base.metadata.create_all(engine)

metadata = MetaData(bind=engine)

#Base.meta = MetaData(engineInv)
###########Low performance##############
# Base.metadata.reflect(engineInv)
end = timer()
print "engine created", (end - start)

start = end

inspector = inspect(engine)


end = timer()
print "engine inspected", (end - start)
print "done"

    


#print Events.__table__.columns.keys()
print Transaction.__table__.columns.keys()


if __name__ == '__main__':

    pass

