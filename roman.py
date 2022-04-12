import unittest


def rom_to_dec(roman: str) -> int:
    # YOUR CODE HERE
    return 1


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

