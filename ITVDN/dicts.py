if __name__ == '__main__':
    '''
    my_dict = {'key': "value", 10: True, 0.2: "hello"}
    print(my_dict)
    print(my_dict.get('ter', 'NO'))
    #my_dict.clear()
    print(my_dict.items())
    #my_dict.pop('key')
    print(my_dict.pop('key'))
    print(my_dict.popitem())
    print(my_dict)
    my_dict.update({5: "world"})
    print(my_dict)
    print(my_dict.values())

#Посчитать с помощью словаря сколько раз элемент повторяется в списке
my_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5]
value_to_count = 1
count_dict = {value_to_count : 0}
for elem in my_list:
    if elem == value_to_count:
        count_dict[value_to_count] +=1
print(count_dict)

#...элементЫ...
my_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5]
count_dict = {}
for elem in my_list:
    if  elem in count_dict:
        count_dict[elem] +=1
    else:
        count_dict[elem] = 1
for key, value in count_dict.items():
    print("Key:", key, "   q-ty:", value)


#Пройтись по словарю и вывести все значения, у которых четный ключ
my_list = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
for key, val in my_list.items():
    if key % 2 == 0:
        print(key, val)
'''

#Удалить все ключи, значения которых начинается с буквы а
d = {"alice": 35, "mark": 15, "april": 56, "john": 15}
new_d = {}
for name, age in d.items():
    if name[0] != "a":
        new_d[name] = age
print(new_d)