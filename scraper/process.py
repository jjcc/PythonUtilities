# -*- coding: UTF-8 -*-
import re
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declare import Transaction, Base, Person
import datetime



re_p = re.compile(ur'([-]*\d+[0-9-_\.]*\d+)\b(?![-_\.])', re.UNICODE)


def get_dg(inp):
    """
    extract digit part of a string. could be a price or date string
    :param inp: sting as input
    :return: digits along with sign
    """
    output = ""
    matchObj = re_p.search(inp)
    if matchObj:
        output = matchObj.group(1)
    else:
        print "No match!!"

    return output


def process(l,dbengine, consultant):
    # print l
    lst = l.split(',')
    # name
    n = lst[0]
    matchObj = re.match(r'(.*)\((.+)\)', n, re.M | re.I)
    if matchObj:
        sname = matchObj.group(1)
        scode = matchObj.group(2)
    else:
        print "No match!!"

    # price
    bp = get_dg(lst[1])
    sp = get_dg(lst[3])

    dbp = float(bp)
    dsp = float(sp)
    dper = round((dsp - dbp) * 100 / dbp, 2)

    # date
    dt_b = get_dg(lst[2])
    dt_s = get_dg(lst[4])

    # quantities
    q = lst[5]
    # percentage
    per = get_dg(lst[6])
    winstr = lst[7][0:6]
    win = 0 if winstr == '跑输' else 1


    print "name %s, code %s ,bp %s, dtb %s, sp %s,dts %s, q %s, per %s, cal %f, iswin? %d" % (
    sname, scode, bp, dt_b, sp, dt_s, q, per, dper, win)
    # print len(lst),n



    # Insert an Address in the address table
    trans = Transaction()
    v1 = u'云南白药(SZ.000538)'
    v2 = sname

    # 云南白药(SZ.000538),平均 69.13 买入,2016-07-07 开仓,平均 66.91 卖出,2016-07-08 平仓,25000,-3.21%,跑输大盘###
    trans.name = sname.decode('utf8')
    trans.symbol = scode
    trans.buy_price = bp
    trans.buy_date = datetime.date(2016, 7, 7)
    trans.sell_price = sp
    trans.sell_date = datetime.date(2016, 7, 8)
    trans.quantity = q
    trans.gain_percentage = per
    trans.win_market = win
    trans.person = consultant
    session.add(trans)
    session.commit()

    pass


def process_epoch(l):
    """
    convert the epoch to date
    :param l:
    :return:
    """

    regex = re.compile(ur'(\d+)', re.UNICODE)
    m = regex.search(l)
    epoch = m.group(0)
    epochf = int(epoch) / 1000

    v = time.localtime(epochf)
    #print v
    dt = time.strftime('%Y-%m-%d', time.localtime(epochf))
    print dt, "wkday", v.tm_wday
    pass



cid = 38612


engine = create_engine('sqlite:///trade.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
engine.raw_connection().connection.text_factory = str

DBSession = sessionmaker(bind=engine)
session = DBSession()


fname = "record_%d.txt"%cid
#fname_epoch = "epoches.txt"

f = open(fname)
#f = open(fname_epoch)
count = 0

new_person = Person()
new_person.cid = cid

session.add(new_person)
# session.commit()
for line in iter(f.readline, b''):
    print count,
    process(line,engine,new_person)

    #process_epoch(line)
    count += 1

    # while (line = f.readline()):
    #    print line
