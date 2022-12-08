class Salary:
    def __init__(self, salary):
        self.salary = salary

    def raise_salary(self):
        if self.salary <= 8999:
            return self.salary * 0.1


class RaiseAnnualSalary(Salary):
    def raise_salary(self):
        amount = super().raise_salary()
        if amount:
            return (12 * amount) * 0.1
        else:
            return (12 * amount) * 0
