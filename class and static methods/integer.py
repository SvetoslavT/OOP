class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, num: float):
        try:
            return cls(int(num))
        except ValueError:
            return "value is not a float"

    @classmethod
    def from_string(cls, string: str):
        if string != str:
            return "wrong type"
        return cls(int(string))

    @staticmethod
    def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

    @classmethod
    def from_roman(cls, roman: str):
        return cls(cls.roman_to_int(roman))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
