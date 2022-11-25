import re


class Profile:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.__name}" and password: {"*" * len(self.password)}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if 5 > len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        find_upper = re.findall('[A-Z]', value)
        find_digit = any(char.isdigit() for char in value)
        if not find_digit or not find_upper:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value


profile_with_invalid_password = Profile('My_username', 'My-password')
