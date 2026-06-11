# def print_numbers(limit):
#     for i in range(limit):
#         print(i)

# num = int(input('Enter number: '))
# print_numbers(num)

###

# def plural(x):
#     if x < 0:
#         return x * 2
#     else:
#         return x * 3
    
# def main():
#     for i in range(-5, 5):
#         print('For number {}'.format(i), ' plural is {}'.format(plural(i)), sep='')

# main()

###

# def foo(a=0, b=0, c=0):
#     return (a + b + c) / 3

# num = 1
# a = 0
# b = 0
# c = 0
# while num > 0:
#     num = int(input('Enter number: '))
#     a = b
#     b = c
#     c = num
#     print('The middle is: {}'.format(foo(a, b, c)))

###

# def greeting(name='Az'):
#     print('Hello, {}!'.format(name))

# greeting()

###

# def funk_1(x=-5, y=5, s=0.5, operation='+'):
#     for i in range(x, y):
#         if operation == '+':
#             print(i+s)
#         elif operation == '-':
#             print(i-s)
#         elif operation == '*':
#             print(i*s)
#         elif operation == '/':
#             print(i/s)

# def funk_2(operation):
#     funk_1(operation=operation)        

# funk_2(operation='*')

###

def sum(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Error: division by zero'
    else:
        return x / y
    
def calculator(x, y, operation):
        if operation == '+':
            return sum(x, y)
        elif operation == '-':
            return substract(x, y)
        elif operation == '*':
            return multiply(x, y)
        elif operation == '/':
            return divide(x, y)
        else:
            return 'Error: invalid operation'
        
def calculate():
    while True:
    
        input_x = float(input('Enter first number: '))
        input_y = float(input('Enter second number: '))
        input_operation = input('Enter operation (+, -, *, /): ')
        if input_operation == 'exit':
            print('Exiting calculator...')
            break
        if input_operation not in ['+', '-', '*', '/']:
            print('Invalid operation. Please try again.')
            continue

        result = calculator(input_x, input_y, input_operation)
        print('Result: {}'.format(result))

calculate()