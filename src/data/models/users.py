class User:
    """
    Class for building basic user data
    """

    def __init__(self, age: int = None, name: str = None, lastname: str = None, email: str = None, gender: str = None) -> None:
        self.__age = age
        self.__name = name
        self.__lastname = lastname
        self.__email = email
        self.__gender = gender

    def get_name(self) -> str:
        """
            Getter for Name of user
        Returns:
            str: self name
        """
        return self.__name

    def get_age(self) -> int:
        """
            Getter for user Age
        Returns:
            int: self Age
        """
        return self.__age

    def get_lastname(self) -> str:
        """
            Getter for lastname
        Returns:
            str: self last_name
        """
        return self.__lastname

    def get_email(self) -> str:
        """
        Getter for Email string.
        """
        return self.__email

    def get_gender(self) -> str:
        """
            Getter for gender of user
        Returns:
            str: self Gender.
        """
        return self.__gender

    def set_name(self, name: str):
        """
        Setting user Name data to __init__ 

        Args:
            gender (str): Name data of user.

        Returns:
            self: Return self.
        """
        self.__name = name
        return self

    def set_age(self, age: int):
        """
        Setting user Age data to __init__ 

        Args:
            gender (str): Age data of user.

        Returns:
            self: Return self.
        """
        self.__age = age
        return self

    def set_lastname(self, lastname: str):
        """
        Setting user Lastname data to __init__ 

        Args:
            gender (str): Lastname data of user.

        Returns:
            self: Return self.
        """
        self.__lastname = lastname
        return self

    def set_email(self, email: str):
        """
        Setting user Email data to __init__ 

        Args:
            gender (str): Email data of user.

        Returns:
            self: Return self.
        """
        self.__email = email
        return self

    def set_gender(self, gender: str):
        """
        Setting user gender data to __init__ 

        Args:
            gender (str): Gender data of user. 'male' of 'female'

        Returns:
            self: Return self.
        """
        self.__gender = gender
        return self

    def remove(self) -> None:
        """
        Method for deleting user data
        """
        self.set_age(None)
        self.set_name(None)
        self.set_lastname(None)
        self.set_email(None)
        self.set_gender(None)

    def build_user_obj(self) -> dict:
        """
            Builder of User data object.
        Returns:
            dict: Dict of user data
        """
        user = {
            'name': self.get_name(),
            'lastname': self.get_lastname(),
            'age': self.get_age(),
            'email': self.get_email(),
            'gender': self.get_gender()
        }
        return user
