from xml.etree import ElementTree as ET
import csv
tree = ET.parse('RunPara.xml')
root = tree.getroot()

# for att in root:
#     first = att.find('attval').text
#     for subatt in att.find('children'):
#         second = subatt.find('attval').text
#         print('{},{}'.format(first, second))

xml_to_csv = open('out.csv','w')
list_head=[]
csv_writer = csv.writer(xml_to_csv)
count = 0

for element in root.findall('RunParametersVersion'):
    list_nodes = []


    if count == 0:
        setup = element.find('Setup')
        list_head.append(setup)

        FlowCellRfidTag = element.find('FlowCellRfidTag')
        list_head.append('FlowCellRfidTag')

        ReagentKitRfidTag = element.find('ReagentKitRfidTag')
        list_head.append('ReagentKitRfidTag')

        count+=1


    setup = element.find('Setup').text
    list_nodes.append(setup)

    FlowCellRfidTag = element.find('FlowCellRfidTag').text
    list_nodes.append('FlowCellRfidTag')

    ReagentKitRfidTag = element.find('ReagentKitRfidTag').text
    list_nodes.append('ReagentKitRfidTag')

    csv_writer.writerow(list_nodes)

xml_to_csv.close()

    


