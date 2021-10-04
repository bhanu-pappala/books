import unittest
from collections import Counter

def is_palindrome_permutation(phrase):
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    odd_count = 0
    for i in phrase:
        x = char_num(i)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                odd_count += 1
            else:
                odd_count -= 1

    return odd_count <= 1

def char_num(ch):
    a = ord('a')
    z = ord('z')
    upper_a = ord('A')
    upper_z = ord('Z')
    val = ord(ch)
    if a <= val <= z:
        return val - a
    if upper_a <= val <= upper_z:
        return val - upper_a
    return -1

def is_palindrome_permutation_pythonic(phrase):
    counter = Counter(phrase.replace(' ', '').lower())
    return sum(val % 2 for val in counter.values()) <= 1

class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [is_palindrome_permutation, is_palindrome_permutation_pythonic]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()
