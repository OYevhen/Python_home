# class User:
#     def __init__(self, age, name):
#         self.__age = age  # _protected __private
#         self.name = name
#
#     def setAge(self, age):
#         if age > 0 and type(age) == int:
#             self.__age = age
#         else:
#             print("age must be more than 0 and int")
#
#     def getAge(self):
#         return self.__age
#
#
# u1 = User(23, "JO")
# u1.setAge(33)
#
# print(u1.getAge())
class User:
    def __init__(self, age, name):
        self.__age = age
        self.name = name

    @property
    def age(self):
        return self.__age


    def set_age(self, vozr):
        if vozr > 0:
            self.__age = vozr

den = User(age=23, name="Denis")
den.name = "Deniska"
den.set_age(32)

print(den.age, den.name)
