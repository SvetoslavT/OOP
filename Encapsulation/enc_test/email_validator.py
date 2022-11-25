class EmailValidator:
    def __init__(self, min_length, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):

        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail):

        domains_and_mails = mail.split(".")
        mail_part = domains_and_mails[0]
        domain_part = domains_and_mails[1]
        if domain_part in self.domains:
            if mail_part in self.mails:
                return True
        return False

    def validate(self, email):
        result = email.split("@")
        if self.__is_mail_valid(result[1]) and self.__is_name_valid(result[0]):
            return True
        return False


mails = ["gmail", "softuni"]

domains = ["com", "bg"]

email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.com"))

print(email_validator.validate("georgios@gmail.net"))

print(email_validator.validate("stamatito@abv.net"))

print(email_validator.validate("abv@softuni.bg"))
