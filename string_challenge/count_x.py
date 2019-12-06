# Write your count_char_x function here:
def count_char_x(word, x):
    number_of_times = 0
    for letter in word:
        if letter == x:
            number_of_times += 1
    return number_of_times

# Uncomment these function calls to test your  function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
