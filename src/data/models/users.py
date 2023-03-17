class User:

    def __init__(self, age, name) -> None:
        # database interaction
        self.age = age
        self.name = name


    def remove(self):
        # database interaction
        self.age = None

