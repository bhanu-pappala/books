from collections import Counter
import unittest

def check_permutation_by_sort(a, b):
    if len(a) != len(b):
        return False
    s1 = sorted(a)
    s2 = sorted(b)
    for i in range(len(a)):
        if s1[i] != s2[i]:
            return False
    return True

def check_permutation_by_count(a, b):
    if len(a) != len(b):
        return False
    counter = [0] * 256
    for char in a:
        counter[ord(char)] += 1
    for char in b:
        if counter[ord(char)] == 0:
            return False
        else:
            counter[ord(char)] -= 1
    return True

def check_permutation_pythonic(a, b):
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)

class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
