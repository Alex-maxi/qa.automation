class User:

    def __init__(self, age: int = None, name: str = None, lastname: str = None, email: str = None, gender: str = None) -> None:
        self.__age = age
        self.__name = name
        self.__lastname = lastname
        self.__email = email
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_lastname(self):
        return self.__lastname

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender
    
    def set_name(self, name: str):
        self.__name = name
        return self

    def set_age(self, age: int):
        self.__age = age
        return self

    def set_lastname(self, lastname: str):
        self.__lastname = lastname
        return self

    def set_email(self, email: str):
        self.__email = email
        return self

    def set_gender(self, gender: str):
        self.__gender = gender
        return self
    
    def remove(self):
        # database interaction
        self.set_age(None)
        self.set_name(None)
        self.set_lastname(None)
        self.set_email(None)
        self.set_gender(None)

    def build_user_obj(self):
        user = {
            'name': self.get_name(),
            'lastname': self.get_lastname(),
            'age': self.get_age(),
            'email': self.get_email(),
            'gender': self.get_gender()
        }
        return user
    

