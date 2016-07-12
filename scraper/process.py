# -*- coding: UTF-8 -*-
import re


re_p = re.compile(ur'\b(\d+[0-9-_\.]*\d+)\b(?![-_\.])', re.UNICODE)

def process(l):
    #print l
    lst = l.split(',')
    #name
    n = lst[0]
    matchObj = re.match( r'(.*)\((.+)\)', n, re.M|re.I)
    if matchObj:
        sname =  matchObj.group(1)
        scode =  matchObj.group(2)
    else:
       print "No match!!"
    p = lst[1]
    re_p = re.compile(ur'\b(\d+[0-9-_\.]*\d+)\b(?![-_\.])', re.UNICODE)
    #re_p = re.compile(ur'平均', re.UNICODE)
    matchObj = re_p.search( p)
    if matchObj:
        buy_price =  matchObj.group(1)
    else:
       print "No match!!"

    print "name %s, code %s ,buy_price%s"%(sname,scode,buy_price)
    #print len(lst),n
    pass



fname = "record.txt"

f = open(fname)
count = 0
for line in iter(f.readline, b''):
    print count,
    process(line)
    count +=1

#while (line = f.readline()):
#    print line