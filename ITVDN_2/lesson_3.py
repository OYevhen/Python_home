# x = float(input('x = '))
#

# if x > 0:
#     print('{} is greater than zero'.format(x))
# elif x < 0:
#     print('{} is less than zero'.format(x))
# elif x == 0:
#     print('{} is equal zero'.format(x))
# else:
#     print('Unknown value')


# print('''Chose your destiny:
# 1. Unexpected
# 2. Bad
# 3. Good
# ''')
# choice = int(input('What\'s your choice?: '))
# if choice == 1:
#     print('You are risky!')
# elif choice == 2:
#     print('You are brave!')
# elif choice == 3:
#     print('Ah, coward!')
# else:
#     print('Unexisting path')

# num = int(input('Enter integer: '))
# if num:
#     print('{} is not zero'.format(num))
# else:
#     print('Is zero')


operation = input('''What do you want?: 
1. Add int numbers
2. Subtract int numbers
''')
a = int(input('a = '))
b = int(input('b = '))
if operation == '1':
    print(a + b)
elif operation == '2':
    print(a - b)
else:
    print('Unexisting choice')

# name = input('What\'s your name?: ')
# if name == 'Zhenya':
#     print('Oh, it\'s my name too !')
# else:
#     print('Nice to meet you, {}'.format(name))