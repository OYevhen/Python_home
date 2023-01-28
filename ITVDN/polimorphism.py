# class Paralelogram:
#     def __init__(self, width, length=None):
#         self.width = width
#         self.length = length
#
#     def get_area(self):
#         return self.width * self.length
#
#
# class Square(Paralelogram):
#     def get_area(self):
#         return self.width * self.width
#
# paral = Paralelogram(2, 3)
# print(paral.get_area())
#
# squ = Square(2)
# print(squ.get_area())

def func(data, new_value):
    if isinstance(data, list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add(new_value)
    elif isinstance(data, str):
        if isinstance(new_value, str):
            data += new_value
    return data


print(func([1, 2, 3], 4))
print(func({1, 5, 3}, 4))
print(func("{1, 5, 3}", 4))
print(func("{1, 5, 3}", "4"))

