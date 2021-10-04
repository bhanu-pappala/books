def urlify_algo(string, length):
    char_list = list(string)
    string = ""
    new_index = len(char_list)
    for i in reversed(range(length)):
        if char_list[i] == ' ':
            char_list[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            char_list[new_index - 1] = char_list[i]
            new_index -= 1

    return string.join(char_list)

def urlify_pythonic(string, length):
    return string.rstrip().replace(' ', '%20')

print(urlify_pythonic("much ado about nothing      ", 22))
print(urlify_algo("much ado about nothing      ", 22))

