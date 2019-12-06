# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    index_start = word.find(start)
    index_end = word.find(end)
    if index_start == -1 or index_end == -1:
        return word
    else:
        return(word[index_start + 1: index_end])


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
