import unittest

num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
       '1': 4, '2': 9, '3': 40, '4': 90, '5': 400, '6': 900}
pair = {'IV': '1', 'IX': '2', 'XL': '3', 'XC': '4', 'CD': '5', 'CM': '6'}


def rom_to_dec(roman_numeral: str) -> int:

    roman_numeral = convert_doubles(roman_numeral)

    sum = 0
    for char in roman_numeral:
        sum += num[char]

    return sum


def convert_doubles(s: str) -> str:
    if len(s) == 1:
        return s

    out = s
    for i in range(1, len(s)):
        if num[s[i-1]] < num[s[i]] and i < len(s)-1:
            out = s[:i-1] + pair[s[i-1]+s[i]] + s[i+1:]

        elif num[s[i - 1]] < num[s[i]] and i == len(s) - 1:
            out = s[:i - 1] + pair[s[i - 1] + s[i]]

    return out


class TestRomanNumerals(unittest.TestCase):
    def test(self):

        numerals = {}
        with open('numerals') as file:
            for line in file.readlines():
                line = line.strip()
                words = line.split(',')
                numerals[words[1]] = int(words[0])

        for numeral in numerals:
            exp = numerals[numeral]
            act = rom_to_dec(numeral)
            self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()
