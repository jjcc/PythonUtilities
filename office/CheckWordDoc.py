from docx import Document
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table

from docx.document import Document as _Document






disable_run_print = 1;

pcount =0
def process_run(run):
    text = run.text
    if disable_run_print == 0:
        print ">>>>run: len of text:%d"%len(text)
    pass


def process_para(para , proc_r, opt = None):
    """

    :param para:
    :param proc_r:
    :return:
    """
    global pcount
    pcount += 1
    print pcount
    text = para.text
    leading_txt = text[:20]
    len_text = len(text)

    if text == "":
        return

    #print para
    runs = para.runs
    no_runs = len(runs)
    print ">>para text: %s, length: %d, runs: %d"%(leading_txt, len_text,no_runs)

    if opt != None:
        pass


    for r in runs:
        proc_r(r)

'''
copy from https://github.com/python-openxml/python-docx/issues/40
'''
def iter_block_items(parent):
    """
    Generate a reference to each paragraph and table child within *parent*,
    in document order. Each returned value is an instance of either Table or
    Paragraph. *parent* would most commonly be a reference to a main
    Document object, but also works for a _Cell object, which itself can
    contain paragraphs and tables.
    """
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
        # print(parent_elm.xml)
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

#fn = "Platinum - Simulated  Survey Report Template 2016 -  FINAL  SPANISH.docx"
fn = "Gold - Simulated Survey Report Template 2016 - FINAL.docx"
doc = Document(fn)

#docx.text.paragraph.Paragraph[source]

if doc is not None:



    #paras = doc.paragraphs
    #print len(paras)

    # for p in paras:
    #     process_para(p,process_run)
    #
    #     pass

    for block in iter_block_items(doc):
        #print('found one')
        if isinstance(block, Paragraph):
            process_para(block, process_run)
        else:
            print( '**************<table>')