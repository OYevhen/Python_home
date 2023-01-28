class Animal(object):
    def __init__(self):
        self.run = False
        self.fly = False

    def print_abilities(self):
        print(type(self).__name__ + ":")
        print("Can run:", self.run)
        print("Can fly:", self.fly)
        print()


class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.fly = True


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.run = True


class Pegasus(Bird, Horse):
    pass


pegas = Pegasus()
pegas.print_abilities()

tweet = Bird()
tweet.print_abilities()