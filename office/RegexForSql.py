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



if  __name__ == "__main__":
    sql_statement = '''
SELECT column1, column2, colume3
FROM table_name
WHERE condition
GROUP BY group; 
'''

    result = match_sql(sql_statement)
    print "Select: %s, From:%s, Where:%s, Group:%s"%(result[KEY_S], result[KEY_F], result[KEY_W],result[KEY_G])
