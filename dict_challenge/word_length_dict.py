# Write a function named word_length_dictionary that takes a list of strings named words as a parameter.
# The function should return a dictionary of key/value pairs where
# every key is a word in words and every value is the length of that word.


def word_length_dictionary(words):
    word_len = {}
    for word in words:
        word_len[word] = len(word)
    return word_len


print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))
