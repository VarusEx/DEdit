from xml.dom import minidom
import FileHelper


xml_data = []
xml_color = []
xml_basic = []


def read_keywords_from_xml():
    xml_doc = minidom.parse(FileHelper.find_way_to_file("keywords.xml"))

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


def read_options_from_xml():
    xml_doc = minidom.parse(FileHelper.find_way_to_file("options.xml"))

    xml_color.append([])
    for item in xml_doc.getElementsByTagName('highlight')[0].getElementsByTagName("item"):
        xml_color[0].append(item.attributes["color"].value)
    xml_basic.append([])
    for item in xml_doc.getElementsByTagName('basic')[0].getElementsByTagName("gothic_src"):
        xml_basic[0].append(item.attributes["root"].value)
