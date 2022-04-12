import unittest
import roman


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
            act = roman.rom_to_dec(numeral)
            self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()