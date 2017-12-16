import collections
import xmltodict

typeNameHash = {}

def process_complex(node):
    '''
    process complex type node list
    '''
    print "Now complex"
    for n in node:
        #print n
        if n.has_key('xsd:sequence'):
            seq = n['xsd:sequence']
            if seq.has_key('xsd:element'):
                new_node = seq['xsd:element']
                process_one_element(new_node)
            else:
                if isinstance(seq, collections.OrderedDict):
                    process_complex([seq])
        elif n.has_key('xsd:all'):
            #print  "All one in complex"
            all_node = n['xsd:all']['xsd:element']
            if isinstance(all_node, collections.OrderedDict) and all_node.has_key('xsd:complexType'):
                process_complex([all_node['xsd:complexType']])
                return

            for ele in all_node:
                #print ele
                if isinstance(ele, collections.OrderedDict):
                    process_one_element(ele)
                else:
                    print ">>>>Interesting case"
                    print ele

        elif n.has_key('xsd:choice'):
            choice = n['xsd:choice']['xsd:element']
            for ele in choice:
                if isinstance(ele, collections.OrderedDict):
                    process_one_element(ele)
                else:
                    print ele
        elif isinstance(n, collections.OrderedDict) and n.has_key('xsd:complexType'):
            complex_node = n['xsd:complexType']
            process_complex([complex_node])
        else:
            print ">>>Another interesting case"
            print n

def process_element(node):
    '''
    process element type, by building a hash map, with key of type, value a list of names
    '''
    for elem in node:
        process_one_element(elem)

def process_one_element(node):
    '''
    process one element of name, type pair which is useful node
    '''
    #print "one element"
    if not node.has_key('@type'):
        return
    eletype = node['@type']
    elename = node['@name']
    #print elename
    if not typeNameHash.has_key(eletype):
        typeNameHash[eletype] = []
    tag_list = typeNameHash[eletype]
    if elename in tag_list:
        return # no duplication
    tag_list.append(elename)


def process_simple(node):
    '''
    process simpleType, node[0] is 'simpleType', node[1] is a list of OdrderedDict
    '''
    for n in node[1]:
        print "Now simple one"
        #for k,v in n.items():
        #    print k, ":", v
        print n
        pass

def process(node, type):
    '''
    process a node
    '''
    if type == 'xsd:complexType':
        process_complex(node)
        return

    if type == 'xsd:element':
        process_element(node)
        return
    
    process_simple(node)





count = 0
if __name__ == "__main__":
    file_name = 'shipment.xsd'
    file_xml = open("data\\" + file_name, 'r')
    xml_data = file_xml.read()
    dict_res = xmltodict.parse(xml_data)
    nodes = dict_res['xsd:schema'].items()
    for n in nodes:
        print ">>>%d:\n"%count
        if not(n[0] in ['xsd:complexType', 'xsd:element', 'xsd:simpleType']):
            continue
        process(n[1], n[0])

        count += 1
    print "done:,count %d"%count
    for k, v in typeNameHash.iteritems():
        listString = "Arrays.asList("
        for e in v[:-1]:
            listString += "\"" + e+ "\","
        listString += "\"" + v[-1]+ "\"));"    



        print "m.put(\"%s\", %s"%(k, listString)

    print "done\n"	