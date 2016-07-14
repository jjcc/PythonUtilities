# -*- coding: UTF-8 -*-
import re
import time

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


def process(l):
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

    print "name %s, code %s ,bp %s, dtb %s, sp %s,dts %s, q %s, per %s, cal %f" % (
    sname, scode, bp, dt_b, sp, dt_s, q, per, dper)
    # print len(lst),n
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


fname = "record.txt"
fname_epoch = "epoches.txt"

# f = open(fname)
f = open(fname_epoch)
count = 0
for line in iter(f.readline, b''):
    print count,
    #     process(line)

    process_epoch(line)
    count += 1

    # while (line = f.readline()):
    #    print line
