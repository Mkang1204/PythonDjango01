import xml.etree.ElementTree as et
import pandas as pd

def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None
 
 
def main():
    """ main """
    parsed_xml = et.parse("RunPara.xml")
    dfcols = ['Runpara', 'FlowCell', 'Ref', 'RunID']
    df_xml = pd.DataFrame(columns=dfcols)
 
    for node in parsed_xml.getroot():
        name = node.attrib.get('RunParameters')
        email = node.find('Setup')
        phone = node.find('FlowCellRfidTag')
        street = node.find('ReagentKitRfidTag')
 
        df_xml = df_xml.append(
            pd.Series([name, getvalueofnode(email), getvalueofnode(phone),
                       getvalueofnode(street)], index=dfcols),
            ignore_index=True)
 
    print df_xml
 
main()