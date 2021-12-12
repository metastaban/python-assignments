# Task:

# Count the number of each letter in a sentence.
# -- The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
# -- Write a Python program that;

# 1. takes a sentence from the user,
# 2. counts the number of each letter of the sentence,
# 3. collects the letters/chars as a key and the counted numbers as a value in a dictionary.


def letters_count(s):
    dict_s = dict()
    for i in set(s):
        count = s.count(i)
        dict_a = {i:count}
        dict_s.update(dict_a)
    return dict_s

print(letters_count("hippo runs to us!"))