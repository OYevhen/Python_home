#Python 3.10
# Шестиугольник
'''
import turtle as t

side = 50
for i in range(6):
    t.forward(side)
    t.right(60)
input()
'''
'''
# print("Test")
a = float(input("a = "))
b = float(input("b = "))
if a == b:
    print("Дана фігура - квадрат")
else:
    print("Дана фігура - прямокутник")
'''
'''

car_1 = input("Введіть марку автомобіля 1 ")
car_2 = input("Введіть марку автомобіля 2 ")
car_3 = input("Введіть марку автомобіля 3 ")

class Cars:
    def __init__(self, list_of_cars=[]):
        self.list_of_cars = list_of_cars



list_cars = []
list_cars.append(car_1)
list_cars.append(car_2)
list_cars.append(car_3)

cars = Cars(list_cars)
print("Список авто: {}".format(" та ".join(cars.list_of_cars)))
'''

"""
wheels_count = int(input("Введіть кількість коліс "))
sits = int(input("Введіть кількість місць "))
guns_count = int(input("Введіть кількість зброї "))


class Banderomobil:
    cars_count = 0

    def __init__(self, wheels_count, sits, guns_count):
        self.wheels_count = wheels_count
        self.sits = sits
        self.guns_count = guns_count
        Banderomobil.cars_count += 1


    def print_info(self):
        print("Бандеромобіль на {} колесах, призначений для {} людей і {} стволів".format(self.wheels_count, self.sits, self.guns_count ))





car1 = Banderomobil(wheels_count, sits, guns_count)
car1.print_info()
print(car1.cars_count)

car2 = Banderomobil(wheels_count + 1, sits + 1, guns_count + 1)
car2.print_info()
print(car2.cars_count)
"""
'''
input_sentence = input("Введіть речення: ")
sentence_to_compare = input("Введіть речення для порівняння: ")
new_word = input("Введіть нове слово, яке потрібно додати в кінець речення: ")
input_word_to_remove = input("Введіть слово яке потрібно вилучити: ")



class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def to_lower(self):
        self.sentence = self.sentence.lower()

    def remove_word(self, word_to_romove):
        self.word_to_remove = word_to_romove
        self.sentence = str(self.sentence).lower().replace(self.word_to_remove.lower(), "")

    def add_word(self, word_to_add):
        self.word_to_add = word_to_add
        self.sentence = "{}{}".format(self.sentence, self.word_to_add)

    def is_similar(self, sentence_to_compare):
        return self.sentence.lower() == sentence_to_compare.lower()


my_sentence = Sentence(input_sentence)
print(my_sentence.is_similar(sentence_to_compare))

my_sentence.add_word(new_word)
my_sentence.to_lower()
print(my_sentence.sentence)

my_sentence.remove_word(input_word_to_remove)
print(my_sentence.sentence)
'''
'''
name = "Сергій"
new_name = "Степан"
new_last_name = "Бандера"
new_second_name = "Андрійович"

class User:
    count_users = 0

    def __init__(self, name):
        self.name = name
        User.count_users += 1


    def change_username(self, username):
        self.name = username

    @classmethod
    def get_count(cls):
        return cls.count_users

    @staticmethod
    def prepare_name(name, last_name, second_name):
        return (f"{last_name} {name[0]}. {second_name[0]}.")






new_username = User.prepare_name(new_name, new_last_name, new_second_name)

user1 = User(name)
print(user1.name)
print(User.count_users)
print(user1.count_users)
user1.change_username(new_username)
print(user1.name)


user2 = User(name)
print(User.count_users)
print(user2.count_users)
'''
'''
input_database_name = "Користувачі"
input_command_to_execute = "Створити Користувача"


class Database:
    def __init__(self, database_name):
        self.database_name = database_name

    connected_to_database = False
    executed_commands = []

    @staticmethod
    def to_lower(str):
        return str.lower()

    @classmethod
    def add_to_executed_commands(cls, command):
        cls.executed_commands.append(command)

    def connect_to_database(self):
        Database.connected_to_database = True
        print("Під'єднано до бази даних")

    def execute_command(self, command):
        print(command)
        Database.add_to_executed_commands(command)






db = Database(input_database_name)
print(db.database_name)
print(db.connected_to_database)

db.connect_to_database()
print(db.connected_to_database)
print(Database.executed_commands)

lower_command = Database.to_lower(input_command_to_execute)
db.execute_command(lower_command)
print(Database.executed_commands)

'''
'''
input_database_name = "Користувачі"
new_database_name = "Зарплата"


class Database:
    def __init__(self, database_name):
        self.__database_name = database_name
        self._connected_to_database = False

    def get_connected_to_database(self):
        return self._connected_to_database

    def set_connected_to_database(self, connection_state):
        self.connection_state = connection_state
        print(
            "Неможливо змінити значення connected_to_database за допомогою присвоєння. Використайте метод connect_to_database"
            )

    def get_database_name(self):
        return self.__database_name

    def set_database_name(self, value):
        self.__database_name = str(value).upper()

    def connect_to_database(self):
        self._connected_to_database = True
        print("Під'єднано до бази даних")


db = Database(input_database_name)
print(db._connected_to_database)
print(db.get_connected_to_database())
db.set_connected_to_database(True)

db.connect_to_database()
print(db._connected_to_database)
print(db.get_connected_to_database())
#
print(db.get_database_name())
db.set_database_name(new_database_name)
print(db.get_database_name())
'''
'''
input_qa_name = "тестувальник андрій"
input_pm_name = "менеджер тарас"
input_qa_expected_action = "Знаходити помилки"
input_pm_expected_action = "Відправляти листи"
input_qa_task = "Протестувати нову функціональність"

# your code goes here
class User:
    def __init__(self, username, expected_action):
        self._username = username
        self._expected_action = expected_action

    def perform_action(self):
        print("{} виконує дію: '{}'".format(self._username, self._expected_action))

    def get_username(self):
        return self._username

    def set_username(self, value):
        self._username = str(value).title()


class QA(User):
    def __init__(self, username, expected_action, tasks=[]):
        super().__init__(username, expected_action)
        self.tasks = tasks


    def set_task(self, task):
        self.tasks.append(task)


class Manager(User):
    def __init__(self, username, expected_action):
        super().__init__(username, expected_action)

    def perform_action(self):
        print("Зайнятий. Напишіть мені листа з Вашим питанням")


qa = QA(input_qa_name, input_qa_expected_action)
print(qa.get_username())
qa.set_username(input_qa_name)
print(qa.get_username())
qa.perform_action()
print(qa.tasks)
qa.set_task(input_qa_task)
print(qa.tasks)
#
pm = Manager(input_pm_name, input_pm_expected_action)
print(pm.get_username())
pm.set_username(input_pm_name)
print(pm.get_username())
pm.perform_action()
'''