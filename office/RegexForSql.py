import re
"""
For extracting elements of SQL
"""

KEY_S = "s"
KEY_F = "f"
KEY_W = "w"
KEY_G = "g"

def match_sql(statement):
    '''
    Parsing sql statment
    '''
    myregex = re.compile(r"SELECT(.+)FROM(.+)WHERE(.+)", re.DOTALL)
    match = myregex.search(statement)
    groupregex = re.compile(r"GROUP BY(.+)", re.DOTALL)
    matchgroup = groupregex.search(statement)

    seg = {KEY_S:"", KEY_F:"", KEY_W:"", KEY_G:""}

    if matchgroup:
        seg[KEY_G] = matchgroup.group(1)
   

    if match:
        print "Match at index %s, %s" % (match.start(), match.end())
        seg[KEY_S] = match.group(1).strip()
        seg[KEY_F] = match.group(2).strip()
        seg[KEY_W] = match.group(3).strip()

    else:
        print "The regex pattern does not match. :("


    return seg



def split_fields(fields):
    '''
    split fields into a list of field
    '''
    idx = 0
    tl = fields
    while True:

        idx = tl.find(",")
        if idx < 0:
            break
        hdr = tl[0:idx].strip()
        tl = tl[idx+1:-1].lstrip()
        print "h:%s,t:%s"%(hdr,tl)
        if tl.find("iif") == 0:
            idx = tl.find(")") #TODO: should have a subroutine to deal with multiple iif
            tl = tl[idx:-1]
    pass


if  __name__ == "__main__":
    sql_statement = '''
SELECT column1, column2, colume3
FROM table_name
WHERE condition
GROUP BY group; 
'''

    result = match_sql(sql_statement)
    print "Select: %s, From:%s, Where:%s, Group:%s"%(result[KEY_S], result[KEY_F], result[KEY_W],result[KEY_G])

    flds = '''
    column1, column2, colunm3, iif(a,b,c) 
    '''
    split_fields(flds)