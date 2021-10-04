def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False

print(string_rotation("waterbottle", "erbottlewat"))
print(string_rotation("foo", "bar"))
print(string_rotation("foo", "foofoo"))
