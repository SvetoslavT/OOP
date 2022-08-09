class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not (5 <= len(value) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        is_lond_enough = len(value) >= 8
        has_upper_case = any(char.isupper() for char in value)
        has_digit = any(char.isdigit() for char in value)
        if not (is_lond_enough and has_upper_case and has_digit):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self._password = value

    def __str__(self):
        return f'You have a profile with username: "{self._username}" and password: {"*" * len(self._password)}'

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
