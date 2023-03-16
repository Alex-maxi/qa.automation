class User:

    def __init__(self, age) -> None:
        # database interaction
        self.age = age

    def remove(self):
        # database interaction
        self.age = None