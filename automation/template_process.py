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

def generate_output( file_in,file_out, m_dict):
    with open(file_in,"r") as fi:
        template = fi.read()
    context = {"bag":m_dict}
    with open( file_out,"w") as fo:
        compiled_template = pymustache.compiled(template)
        rendered = compiled_template.render(context)
        fo.write(rendered)

    pass

