import unittest


def rom_to_dec(roman_numeral: str) -> int:
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
           '1': 4, '2': 9, '3': 40, '4': 90, '5': 400, '6': 900}

    roman_numeral = convert_doubles(roman_numeral)

    sum = 0
    for char in roman_numeral:
        sum += num[char]

    return sum


def convert_doubles(s: str) -> str:
    # Iterate through all the numerals in the input (roman_numeral) and check for double letters
    for i in range(1, len(s)-1):
        if s[i-1] == 'I' and s[i] == 'V':
            s = s[:i-1] + '1' + s[i+1:]
        if s[i-1] == 'I' and s[i] == 'X':
            s = s[:i-1] + '2' + s[i+1:]
        if s[i-1] == 'X' and s[i] == 'L':
            s = s[:i-1] + '3' + s[i+1:]
        if s[i-1] == 'X' and s[i] == 'C':
            s = s[:i-1] + '4' + s[i+1:]
        if s[i-1] == 'C' and s[i] == 'D':
            s = s[:i-1] + '5' + s[i+1:]
        if s[i-1] == 'C' and s[i] == 'D':
            s = s[:i-1] + '5' + s[i+1:]
        if s[i-1] == 'C' and s[i] == 'M':
            s = s[:i-1] + '6' + s[i+1:]

    if s.startswith('IV'):
        s = '1' + s[2:]

    if s.endswith('IV'):
        s = s[:(len(s)-2)] + '1'

    if s.startswith('IX'):
        s = '2' + s[2:]

    if s.endswith('IX'):
        s = s[:(len(s)-2)] + '2'

    if s.startswith('XL'):
        s = '3' + s[2:]

    if s.endswith('XL'):
        s = s[:(len(s)-2)] + '3'

    if s.startswith('XC'):
        s = '4' + s[2:]

    if s.endswith('XC'):
        s = s[:(len(s)-2)] + '4'

    if s.startswith('CD'):
        s = '5' + s[2:]

    if s.endswith('CD'):
        s = s[:(len(s)-2)] + '5'

    if s.startswith('CM'):
        s = '6' + s[2:]

    if s.endswith('CM'):
        s = s[:(len(s)-2)] + '6'

    return s


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
