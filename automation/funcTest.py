import re
import pymustache
import datetime
import os
import sys
#sys.path.append(os.getcwd())


import itertools

place_holder = "<!-- ph -->"
datestring = datetime.date.today().strftime("%Y%m%d")
replacing = "<div class='row'><a href='%s.html'>%s</a></div>\n"%(datestring,datestring) + place_holder

with open ("data/main.html","r") as main_f:
    main_data = main_f.read()
new_main = main_data.replace(place_holder, replacing)
#print(new_main)
with open ("data/main2.html","w") as output_f:
    output_f.write(new_main)
