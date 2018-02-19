import datetime
import re
import pymustache





def generate_mustache_map(symble_name, count, mdict):
    '''
    generate key/value pairs for mustache template
    :param symbol_name:
    :param count:
    :param mdict:
    :return:
    '''
    datestring = datetime.date.today().strftime("%Y%m%d")
    m = re.match(r"\((\w+)\)", symble_name)
    if (m ):
        sy = m.group(1)
        ks = "s%d"%count
        kimg = "img%d"%count
        image_name= sy + datestring + ".gif"
        mdict[ks] = symble_name
        mdict[kimg] = image_name
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
    context = {toptag:m_dict}
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