import unittest


def rom_to_dec(roman_numeral: str) -> int:
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'F': 4, 'N': 9, 'A': 40}

    roman_numeral = convert_4_and_9(roman_numeral)

    sum = 0
    for char in roman_numeral:
        sum += num[char]

    return sum


def convert_4_and_9(s: str) -> str:
    # Iterate through all the numerals in the input (roman_numeral) and check for double letters
    for i in range(1, len(s)-1):
        if s[i-1] == 'I' and s[i] == 'V':
            s = s[:i-1] + 'F' + s[i+1:]
        if s[i-1] == 'I' and s[i] == 'X':
            s = s[:i-1] + 'N' + s[i+1:]
        if s[i-1] == 'X' and s[i] == 'L':
            s = s[:i-1] + 'A' + s[i+1:]

    if s.startswith('IV'):
        s = 'F' + s[2:]

    if s.endswith('IV'):
        s = s[:(len(s)-2)] + 'F'

    if s.startswith('IX'):
        s = 'N' + s[2:]

    if s.endswith('IX'):
        s = s[:(len(s)-2)] + 'N'

    if s.startswith('XL'):
        s = 'A' + s[2:]

    if s.endswith('XL'):
        s = s[:(len(s)-2)] + 'A'

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


