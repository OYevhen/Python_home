class User:
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.user_type = user_type

    def access_database(self):
        if self.user_type == "superuser":
            return "access granted"
        else:
            return "access denied"

class SuperUser(User):
    def __init__(self, user_type="superuser"):
        self.user_type = user_type

u1 = User(23, "Usia", "user")
print(u1.access_database())

u2 = User(13, "Zed", "superuser")
print(u2.access_database())

u3 = SuperUser()
print(u3.access_database())
