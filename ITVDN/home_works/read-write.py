# filename = "my_text.txt"

# text_file = open(filename, 'r')
# txt = text_file.read()
# text_file.close()
# print(txt)

# with open(filename, 'r') as text_file:
#     text = text_file.read()
# print(text)

# filename2 = "my_text_2"
# # text_file = open(filename2, "w")
# # txt = "Some how"
# # text_file.write(txt)
# # text_file.close()
#
# with open(filename2, "w") as text_file:
#     txt = "123qwr"
#     text_file.write(txt)

# import json
# filename = 'my_file.json'
# with open(filename, "r") as file:
#     data = json.load(file)
#
# data.append({"name": "Alex", "age": 45})
#
# print(data)
#
# with open('my_file2.json', "w") as file:
#     json.dump(data, file)

from xml.dom import minidom
# from xml.etree import ElementTree
# # my_doc = minidom.parse("my_file.xml")
# # items = my_doc.getElementsByTagName("item")
# # print(items)
#
# data = ElementTree.Element("data")
# items = ElementTree.SubElement(data, "items")
# item1 = ElementTree.SubElement(items, "item")
# item2 = ElementTree.SubElement(items, "item")
# item1.set("name", "item1")
# item2.set("name", "item2")
# item1.text = "item1abc"
# item2.text = "item2abc"
#
# my_data = ElementTree.tostring(data)
# with open("items2.xml", "wb") as my_file:
#     my_file.write(my_data)

import csv

with open('data.csv', "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    data = [row for row in csv_reader]

data.append(["Mike", "35", "male"])
print(data)

with open("data.csv", "w") as data_file:
    csv_writer = csv.writer(
        data_file,
        delimiter=","
    )
    for row in data:
        csv_writer.writerow(row)