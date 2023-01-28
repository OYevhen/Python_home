'''
product_price = 600
if product_price > 1000:
    product_price *= 0.9
elif product_price > 500:
    product_price *= 0.95
elif product_price > 100:
    product_price *= 0.97
print(product_price)

value_str = "Hello"
print(None if value_str =="" else value_str)
print(None if not value_str else value_str)
'''

first_value = j
second_value = 9
operator = "/"
if first_value is None or second_value is None:
    print("Can't divide None values")
else:
    if operator == "+":
        print(first_value + second_value)
    elif operator == "-":
        print(first_value - second_value)
    elif operator == "/":
        if second_value == 0:
            print("Can't divide by 0")
        else:
            print(first_value / second_value)
    elif operator == "*":
        print(first_value * second_value)
    else:
        print("Unknown error")