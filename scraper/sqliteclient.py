# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declare import Transaction, Base, Person
import datetime

engine = create_engine('sqlite:///trade.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Insert a Person in the person table
new_person = Person()
new_person.name = "lou"

session.add(new_person)
session.commit()

# Insert an Address in the address table
trans = Transaction( person=new_person)

#云南白药(SZ.000538),平均 69.13 买入,2016-07-07 开仓,平均 66.91 卖出,2016-07-08 平仓,25000,-3.21%,跑输大盘###
trans.name = u"云南白药"
trans.symbol = u"SZ.000538"
trans.buy_price = 69.13
trans.buy_date = datetime.date(2016,7,7)
trans.sell_price = 66.91
trans.sell_date = datetime.date(2016,7,8)
trans.quantity = 250
trans.gain_percentage = -3.21
trans.win_market = 0
trans.person = new_person
session.add(trans)
session.commit()