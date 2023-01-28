'''
class Human:
    def __init__(self, age, name, gender):
        self.let = age
        self.imia = name
        self.pol = gender

    def get_name(self):
        return self.imia

    def get_age_and_name(self):
        return self.let, self.get_name()

human_1 = Human(age=13, gender="male", name="john")
print(human_1.get_age_and_name())
'''

class Human:
    def __init__(self, a):
        self.age = a

    def say_hello(self):
        print("Hello, I am {} years old".format(self.age))

# boy = Human(a=25)
# boy.say_hello()

class HumanEx(Human):
    # pass
    def __init__(self, a, n):
        super().__init__(a)
        self.name = n

    def say_hello(self):
        print("Hello, and I am {}, I have {} years old".format(self.name, self.age))


# girl = HumanEx(a=15, n="Ira")
# girl.say_hello()

class A:
    def __init__(self):
        self.a = 10

class B:
    def __init__(self):
        self.b = 5

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

c = C()
print(c.a)
print(c.b)