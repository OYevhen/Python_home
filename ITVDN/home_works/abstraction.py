"""class Data:
    def __init__(self, country, name, age, gender, height, weight):
        self.country = country
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f"country {self.country}, name {self.name}, age {self.age}, gender {self.gender}, " \
               f"height {self.height}, weight {self.weight}"

class Database:
    def __init__(self):
        self.__db = []

    def read_data(self, criteria):

        #пробежаться по всем элементам списка self.__db
         #   сопоставляем ключи из criteria с реквизитами Data
          #  при совпадении сохранять в список и вернуть список совпадающих значений

        result = []
        for i in self.__db:  #1
            # print(i.__dict__)
            is_equal = True
            for k, v in criteria.items():   #2
                if i.__dict__.get(k) != v:
                    is_equal = False
                    break
            if is_equal:
                result.append(i)

        return result

    def write_data(self, element):
        self.__db.append(element)

db = Database()
data1 = Data("UA", "Azz", 23, "M", 183, 62)
data2 = Data("EN", "Sas", 23, "M", 144, 32)
data3 = Data("ES", "Vas", 24, "F", 144, 32)
db.write_data(data1)
db.write_data(data2)
db.write_data(data3)
print(db.read_data({'gender': "M"}))


"""

