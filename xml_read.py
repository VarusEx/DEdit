from xml.dom import minidom
import api


xml_data = []


def read_keywords_from_xml(self):
    xml_doc = minidom.parse(api.find_way_to_file("keywords.xml"))

    xml_data.append([])
    # While to takes elements from xml file
    for item in xml_doc.getElementsByTagName('keywords')[0].getElementsByTagName("item"):
        xml_data[0].append(item.attributes["word"].value)
    xml_data.append([])
    for item in xml_doc.getElementsByTagName('opertors')[0].getElementsByTagName("item"):
        xml_data[1].append(item.attributes["symbol"].value)
    xml_data.append([])
    for item in xml_doc.getElementsByTagName('function')[0].getElementsByTagName("item"):
        xml_data[2].append(item.attributes["func"].value)
    xml_data.append([])


def read_config_from_xml():
    pass
