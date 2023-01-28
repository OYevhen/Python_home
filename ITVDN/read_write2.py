# import random
#
# letters = "qwertyuiopasdfghjklzxcvbnm"
# random_letters = ""
# string_len = len(letters)-1
#
# while len(random_letters) < string_len:
#     random_letter = letters[random.randint(0, len(letters)-1)]
#     random_letters += random_letter
#
# print(random_letters)
#
# with open("random_letters", "w") as file:
#     file.write(random_letters)
# import random
# import datetime
# import json
#
# users = ["Archi", "Kate", "Al", "Mia"]
# users_list = []
# for user in users:
#     users_list.append({'name': user, 'age': random.randint(1, 99)})
# data = {
#     'data': users_list,
#     'current_date': datetime.datetime.now().strftime("%d;%m;%y")
# }
# filename = "users data {current_date}.json".format(current_date=data["current_date"])
#
# with open(filename, "w") as json_file:
#     json.dump(data, json_file)

# import json
# import csv
#
# with open("users data 02;11;22.json", "r") as file:
#     data = json.load(file)
#
# rows = []
#
# for user in data['data']:
#     rows.append(list(user.values()))
# rows = [list(data["data"][0].keys())] + rows
#
# with open("user_data_{date}.csv".format(date=data["current_date"]), "w") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")
#     for row in rows:
#         csv_writer.writerow(row)

from xml.etree import ElementTree
import csv

with open("user_data_02;11;22.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    data = [row for row in reader]

columns = data[0]
users = data[1:]

xml_data = ElementTree.Element('data')
items_holder = ElementTree.SubElement(xml_data, "users")
items = [ElementTree.SubElement(items_holder, "user") for i in range(len(users))]
for j in range(len(users)):
    item = items[j]
    for k in range(len(columns)):
        item.set(columns[k], users[j][k])

xml_file = ElementTree.tostring(xml_data)
with open('userx.xml', 'wb') as file:
    file.write(xml_file)