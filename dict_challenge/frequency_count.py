# Write a function named frequency_dictionary that takes a list of elements named words as a parameter.
# The function should return a dictionary containing the frequency of each element in words.


def frequency_dictionary(words):
    freqs = {}
    for word in words:
        if word not in freqs:
            freqs[word] = 0
        freqs[word] += 1
    return freqs


print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0, 0, 0, 0, 0]))
