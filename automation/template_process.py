import datetime
import re
import pymustache


STOCK_COUNT = 0


def generate_mustache_map(symble_name, count, mdict):
    '''
    generate key/value pairs for mustache template
    :param symbol_name:
    :param count:
    :param mdict:
    :return:
    '''
    global STOCK_COUNT
    datestring = datetime.date.today().strftime("%Y%m%d")
    m = re.match(r"\(([\w|\$]+)\)", symble_name)
    if (m ):
        sy = m.group(1)
        if sy.find('$') != -1:
            sy = sy.replace("$","x")
    #else:
    #    sy = symble_name
        ks = "s%d"%count
        kimg = "img%d"%count
        kcnt = "cnt%d"%count
        image_name= sy + datestring + ".gif"
        mdict[ks] = symble_name
        mdict[kimg] = image_name
        STOCK_COUNT += 1
        mdict[kcnt] = STOCK_COUNT
    return

def generate_output( file_in,file_out, m_dict,toptag="bag"):
    '''
    Generate output file
    :param file_in:
    :param file_out:
    :param m_dict: rendering data, could be dictionary or list
    :param toptag: the root tag inside tempalte
    :return:
    '''
    with open(file_in,"r") as fi:
        template = fi.read()

    datestring = datetime.date.today().strftime("%Y-%m-%d")
    context = {toptag:m_dict,"date":datestring}
    with open( file_out,"w") as fo:
        compiled_template = pymustache.compiled(template)
        rendered = compiled_template.render(context)
        fo.write(rendered)

    pass

def mod_dict(bag,prefix):
    '''
    add prefix to image part of a mustache dictionary. The prefix normally is a folder name with date information
    :param bag:
    :param prefix:
    :return:
    '''
    bag_mod = {}
    for k, v in bag.items():
        #print("key:%s,value:%s" % (k, v))
        if re.search(r"img", k):
            bag_mod[k] = prefix + v
        else:
            bag_mod[k] = v
    return bag_mod

def get_stock_count():
    global STOCK_COUNT
    return STOCK_COUNT