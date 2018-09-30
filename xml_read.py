from xml.dom import minidom
import api


xmldata = []


def read_keywords_from_xml(self):
    way = api.find_way_to_file(self, "keywords.xml")
    xml_doc = minidom.parse(way)

    self.xmldata.append([])
    # While to takes elements from xml file
    for item in xml_doc.getElementsByTagName('keywords')[0].getElementsByTagName("item"):
        self.xmldata[0].append(item.attributes["word"].value)
    self.xmldata.append([])
    for item in xml_doc.getElementsByTagName('opertors')[0].getElementsByTagName("item"):
        self.xmldata[1].append(item.attributes["symbol"].value)
    self.xmldata.append([])
    for item in xml_doc.getElementsByTagName('comment')[0].getElementsByTagName("item"):
        self.xmldata[2].append(item.attributes["symbol"].value)
    self.xmldata.append([])
    for item in xml_doc.getElementsByTagName('braces')[0].getElementsByTagName("item"):
        self.xmldata[3].append(item.attributes["key"].value)
    self.xmldata.append([])
    for item in xml_doc.getElementsByTagName('function')[0].getElementsByTagName("item"):
        self.xmldata[4].append(item.attributes["func"].value)
    self.xmldata.append([])
