import re


def match_sql(statement):
    '''
    Parsing sql statment
    '''
    myregex = re.compile(r"SELECT(.+)FROM(.+)WHERE(.+)", re.DOTALL)
    match = myregex.search(statement)

    if match:
        print "Match at index %s, %s" % (match.start(), match.end())
        return (match.group(1), match.group(2), match.group(3))
    else:
        print "The regex pattern does not match. :("
        return (None, None, None)





if  __name__ == "__main__":
    sql_statement = '''
SELECT column1, column2, colume3
FROM table_name
WHERE condition; 
'''

    (s, f, w) = match_sql(sql_statement)
    print "Select: %s, From:%s, Where:%s"%(s, f, w)
