import xmltodict
import json
 
with open('Pro.xml') as in_file:
    xml = in_file.read()
    def lsttostr(lst):
      str = ' '
      return(str.join(lst))
    lst = xml.split()
    doc = lsttostr(lst)
    fh = open("Pro.xml",'w')
    fh.write(doc)
    fh.close()
json = json.dumps(xmltodict.parse(doc))
print(str(json))

fh = open('Output.xml','w')
fh.write(json)
fh.close()
  
