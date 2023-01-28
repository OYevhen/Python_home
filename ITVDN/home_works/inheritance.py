# Наследование
# class Cat:
#     def __init__(self, color, cat_type):
#         self.size = None
#         self.color = color
#         self.cat_type = cat_type
#
#     def set_size(self):
#         self.size = "small" if self.cat_type == "indoor" else "undefined"
#
#
# kitten = Cat("white", "indoor")
# kitten.set_size()
# print(kitten.size)
# class Car():
#     def __init__(self, mark, color, capacity):
#         self.mark = mark
#         self.color = color
#         self.capacity = capacity
#
#     @staticmethod
#     def move_front():
#         print("moving front!")
#
#     @staticmethod
#     def move_back():
#         print("move backward!")
#
# class Car2(Car):
#     def left(self):
#         print("turning left!")
#
#     def right(self):
#         print("turning right!")
#
# class Airplain():
#     def __init__(self, model):
#         self.model = model
#
#     def takeoff(self):
#         print("up! up!")
#
# class AirCar(Car2, Airplain):
#     def __init__(self, mark, color, capacity, model):
#         Car2.__init__(self, mark, color, capacity)
#         Airplain.__init__(self, model)
#
# # car = Car2("Audi", "blue", "3.3)
# # # car.move_back()
# # car.left()
#
# # Car.move_back()
#
# my_car = AirCar(mark="As", color="pin", capacity= 5, model="Tes")
# my_car.takeoff()
# my_car.left()

class Cat:
    def __init__(self, color, cat_type):
        self.size = None
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        self.size = "small" if self.cat_type == "indoor" else "undefined"


toha = Cat("white", "indoor")
toha.set_size()
print(toha.size)

class Tiger(Cat):
    def __init__(self, cat_type):
        self.cat_type = cat_type
        self.size = "big" if self.cat_type == "wild" else "undefined"

lukas = Tiger("wild")
print(lukas.size)
