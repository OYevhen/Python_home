a = float(input('1st value: '))
b = float(input('2d value: '))
operation = input('operation : ')
result = None

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
else:
    print('Unexpected value')

if result is not None:
    print('The result is:', result)