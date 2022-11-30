import math


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        return cls(math.ceil(value))

    @staticmethod
    def from_roman(s):
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
        return res

    @staticmethod
    def from_string(value):
        return eval(value)


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")


print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
