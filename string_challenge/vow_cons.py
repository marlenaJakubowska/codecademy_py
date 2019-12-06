# vowels = "aeyoui"
def string_sort(word):
    vowels = "aeyoui"
    word_vowels = ''
    word_cons = ''
    for char in word:
        if char in vowels:
            word_vowels += char
        else:
            word_cons += char
    return word_vowels, word_cons


print(*string_sort("codecool"))
