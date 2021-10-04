from collections import defaultdict

def is_unique_chars_algorithmic(string):
    if len(string) > 128:
        return False
    charset = [None] * 128
    for char in string:
        val = ord(char)
        if charset[val]:
            return False
        charset[val] = True

    return True

def is_unique_chars_pythonic(string):
    return len(set(string)) == len(string)

def is_unique_bit_vector(string):
    if len(string) > 128:
        return False
    
    checker = 0
    for c in string:
        val = ord(c)
        if checker & (1 << val) > 0:
            return False
        checker |= 1 << val
    return True

def is_unique_chars_using_dictionary(string):
    ht = {}
    for char in string:
        if char in ht:
            return False
        ht[char] = 1
    return True

def is_unique_chars_sorting(string: str) -> bool:
    sorted_string = sorted(string)
    last_seen = None
    for k in sorted_string:
        if k == last_seen:
            return False
        last_seen = k
    return True

