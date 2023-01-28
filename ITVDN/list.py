'''
my_list = list("test")
my_list = ['t', 'e', 's', 't']
my_list = ['t', '35', 's', False]
print(my_list)

my_list = [1, 2, 3]
your_list = [4, 5, 6]
#print(my_list[0:8:2])
#my_list.append("11")
print(my_list)
my_list.extend(your_list)
print(my_list)
print(my_list.index(4))
print(my_list[3])
#print(my_list[0:8:3])

your_list.append(my_list)
#my_list.clear()
print(your_list)

my_list = [0, 1, 2, 3, 4, 5]
deleted = my_list.pop(3)
my_list.reverse()
print(my_list)

print(deleted)

a = [5, 2, 1, 4]
a.sort(reverse=True)
b = []
#print(a)

for elem in a:
    b.append(elem)
print(b)

my_list = [1, 2, 3, 4, 5, 6, 7]
even_list = []
for elem in my_list:
    if elem % 2 == 0:
        even_list.append(elem)  #поиск кратных значений
print(even_list)

my_list = [2, 4, 6, 8]
squares_elem = []

for n in my_list:
    squares_elem.append(n**2)
print(squares_elem)

x = [1, 5, -3, -5, 2, 4, -1, -10, 10]
max_elem = x[0]
for elem in x:
    if elem > max_elem:
        max_elem = elem
print("Max: ",  max_elem)
'''
x = [1, 5, -3, -5, 2, 4, -1, -10, 10]
x.sort()
print("min: ", x[0])
x.sort(reverse=True)
print("max: ", x[0])