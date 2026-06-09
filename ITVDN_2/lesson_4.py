# a = int(input('a = '))
# while a != 0:
#     print (a)
#     a -= 1

###

# while True:
#     print('Введите число (0 - выход): ')
#     a = int(input('> '))
#     if a == 0:
#         break
# print('Вы вышли из цикла')

###

# name = None

# while True:
#     print('Existing choices:')
#     print('1. Enter name')
#     print('2. Greet')
#     print('3. Exit')
#     print('')
#     choice = input('What\'s you choice? : ')
#     print('')

#     if choice == '1':
#         print('')
#         name = input('Enter your name: ')
#         print('')
#     elif choice == '2':
#         if name:
#             print('')
#             print(f'Hello, {name}!')
#             print('')
            
#         else:
#             print('')
#             print('You should enter your name first')
#             print('')
#     elif choice == '3':
#         print('')
#         print('Good bye!')
#         break
        
#     else:    
#         print('')
#         print('Unknown choice')
#         print('')

###

# attempts_left = 3
# while attempts_left > 0:
#     attempts_left -= 1
#     password = input('Enter correct password.'
#                      'Attempts left: {} '.format(attempts_left+1))
#     if password == 'qwerty':
#         print('You are welcome!')
#         break
# else: 
#     print('You are blocked!')

###

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

###

# for attempts_left in range(3, 0, -1):
#     password = input('Enter correct password.'
#                      'Attempts left: {} '.format(attempts_left))
#     if password == 'qwerty':
#         print('You are welcome!')
#         break
# else: 
#     print('You are blocked!')

###

# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print('')

###

# n = int(input('Enter width of rectangle: '))
# m = int(input('Enter height of rectangle: '))
# for i in range (m):
#     for j in range(n):
#         print('*', end='')
#     print('')

###

# numbers = [1, 2, 2.2, 3, 3.3, 4, 5.5]
# sum = 0
# for i in numbers:
#     if type(i) == int:
#         sum += i
# print('Sum of integers in list is: {}'.format(sum))

###

# num = int(input('Enter number: '))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print('Factorial of {} is: {}'.format(num, factorial))

###

for i in range (1, 10):
    print('*'*i, end='')
    print('|'*(10-i), end='')
    print('')
    