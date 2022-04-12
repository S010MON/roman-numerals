import unittest


def rom_to_dec(roman_numeral: str) -> int:
    """
    A function that takes a roman numeral 'CXXIV' and converts it to an arabic decimal '124'
    :param roman_numeral: in the form of a string of chars without a break in decending order, where quadruplets
    such as 'IIII' are simplified to the subtractive form 'IV' (5 minus 1)
    :return: an integer value of the numeral
    """
    # YOUR CODE HERE
    return 0


# This test class runs all pairs within the numerals file for testing your code
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
