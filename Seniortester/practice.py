''' dict { Словарь } '''

# person = {'name': 'Alice', 'age': 25, 'city': 'Kyiv'}

# print(person['name'])
# print(person.get('gender', 'female'))

# person['age'] = 22
# print(person['age'])

# person['job'] = 'developer'
# print(person['job'])

# person.pop('city')
# print(person.get('city', 'deleted'))

# del person['job']
# print(person)

# print('---')
# print(person.keys())
# print(person.values())
# print(person.items())

###

# text = 'apple banana apple cherry banana apple'

# counts = {}
# for word in text.split():
#     counts[word] = counts.get(word, 0) + 1

# print(counts)

''' list [ Список ] '''

# fruits = ['apple', 'banana', 'cherry']
# print(list(range(1, 6)))
# print(fruits[0])
# print(fruits[-1])
# print(fruits[1:2])
# print(fruits[::-1])

# print('---')

# fruits.reverse()
# print(fruits)

# print('---')

# fruits.append('mango')
# print(fruits)

# fruits.insert(1, 'grape')
# fruits.insert(1, 'grape')
# print(fruits)

# fruits.remove('grape')
# print(fruits)

# fruits.pop()
# print(fruits)

# print([x**2 for x in range(1, 20) if x % 2 == 0])

# print([[1 if i == j else 0 for j in range(3)] for i in range(3)])

''' tuple ( Кортеж ) '''

# single = (42, )
# rgb = (255, 255, 128, 0)
# r, g, g1, b = rgb
# first, *rest = (1, 2, 3, 4)

# print(rgb.count(255))
# print(rgb.index(255))

# lst = list(rgb)
# tpl = tuple(lst)

# coord = (12, 34, 56)
# a, b, c = coord
# print(a + b + c)

# def min_max(numbers):
#     return min(numbers), max(numbers)

# nums = [3, 1, 7, 2, 9, 4]

# result = min_max(nums)
# print(result)
# print(result[1])

''' str " Строка " '''

# s = 'Alice     '
# print('A' in s)
# print(s[0:2])
# print(s.startswith('Al'))
# print(s.strip(), 'A')
# print(s.strip().endswith('ce'))
# print(s.count('Al'))

# s = 'Alice in wonderland'
# print(s.split(' '))

# s = " Alice, 25, Kyiv "
# s = s.strip()
# s = s.split(',')
# s = s[0].upper()
# print(s)
# clean = s.strip()
# parts = clean.split(',')
# name = parts[0].upper()
# age = parts[1]
# city = parts[2]
# print(f'{name},{age},{city}')

# polindrome = "A man a plan a canal Panama"
# s1 = list(polindrome.replace(' ', '').lower())
# s2 = s1[::-1]
# print(s1 == s2)

# template = "Dear {name}, your order #{order_id} is ready."
# print(template.format(name='Alice', order_id=42))

''' set { Множество } '''

# colors = {'red', 'green', 'blue'}
# unique = set([1, 2, 2, 3, 3])
# empty = set()   # не {} !

# colors.add('yellow')
# print(colors)

# colors.discard('yellow')
# print(colors)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a | b)    # {1, 2, 3, 4, 5, 6}
# print(a & b)    # {3, 4}
# print(a ^ b)    # {1, 2, 5, 6}
# print(a - b)    # {1, 2}

# lst = [1, 2, 2, 3, 3, 3, 4]

# print(sorted(set(lst)))

# a = [1, 2, 2, 3, 4]

# print(len(a) == len(set(a)))

''' abs() '''

# print(abs(-7))      # 7

''' all() '''
# print(all([True, 1, True]))     # True
# print(all([True, 0, 1]))        # False
# print(all([]))                  # True
# print(all(''))                  # True

''' any() '''
# print(any([1, 0, False]))       # True
# print(any([]))                  # False
# print(any(''))                  # False

''' bool() '''
# print(bool(0))                  # False
# print(bool(1))                  # True
# print(bool(''))                 # False
# print(bool('boo'))              # True

''' dict() '''
# print(dict(a=1, b=2))                   # {'a': 1, 'b': 2}
# print(dict([('x', 10), ('y', 100)]))    # {'x': 10, 'y': 100}

''' dir() '''
# print(dir([]))                  # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# print(dir(str))                 # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__','__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

''' enumerate() '''
# print(dict(enumerate(['x', 'y'], start=1)))     # [(1, 'x'), (2, 'y')]

''' help() '''
# help(str.split)                 # Help on method_descriptor: split(self, /, sep=None, maxsplit=-1) unbound builtins.str method  Return a list of the substrings in the string, using sep as the separator string.

''' id() '''
# x = [1, 2]
# y = x
# print(id(x), id(y))                 # 139684897023104 139684897023104
# print(id(y) == id([1, 2]))          # False

''' int() '''
# print(int(3.9))         # 3
# print(int('42'))        # 42

''' isinstance() '''
# print(isinstance(5, int))                       # True
# print(isinstance([], (list, tuple, int)))       # True

''' len () '''
# print(len('hello'))        # 5
# print(len([1, 2, 3]))      # 3

''' max() '''
# print(max(1, 2, 4))         # 4
# print(max('abc'))           # c

''' min() '''
# print(min(1, 2, 4))         # 1
# print(min('abc'))           # a

''' open() '''
# with open('file.txt', 'w') as f:
#     f.write('Hello')

# with open('file.txt', 'r') as f:
#     text = f.read()
#     print(text)

''' pow() '''
# print(pow(2, 10))           # 1024
# print(pow(2, 10, 100))      # 24

''' print() '''
# print(1, 2, sep='-')            # 1-2
# print('ok', end='!!!')          # ok!!!

''' range() '''
# print(list(range(1,6)))             # [1, 2, 3, 4, 5]
# print(list(range(5, 0, -1)))        # [5, 4, 3, 2, 1]
# print(list(range(0, 10, 2)))        # [0, 2, 4, 6, 8]

''' reversed() '''
# print(list(reversed([1, 2, 3])))        # [3, 2, 1]
# print(''.join(reversed('abc')))         # cba

''' round() '''
# print(round(3.14159, 2))        # 3.14
# print(round(3.5))               # 4
# print(round(2.5))               # 2 !!!
# print(round(1234, -2))          #1200

''' set() '''
# print(set({1, 1, 1, 2, 2, 3}))      # {1, 2, 3}
# print(''.join(set('hello')))        # leoh
# print({1, 2} | {2 ,3})              # {1, 2, 3}
# print({1, 2} & {2, 3})              # {2}
# print({1, 2} - {2, 1})              # set()
# print({1, 2} ^ {2, 3})              # {1, 3}

''' sorted() '''
# print(sorted([3, 1, 2]))                    # [1, 2, 3]
# print(sorted([3, 1, 2], reverse=True))      # [3, 2, 1]
# print(sorted(['b', 'a', 'c']))              # ['a', 'b', 'c']

# words = ['b', 'aa', 'ccc']
# print(sorted(words, key=len))               # ['b', 'aa', 'ccc']

''' str() '''
# print(str('42'))                    # 42

''' sum() '''
# print(sum([1, 2, 3]))           # 6
# print(sum([1, 2, 3], 10))       # 16
# print(sum(range(1, 5)))         # 10

''' tuple() '''
# print(tuple('abc'))             # ('a', 'b', 'c')
