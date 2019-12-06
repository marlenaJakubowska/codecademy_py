# Create a function named count_first_letter that takes a dictionary named names as a parameter.
# names should be a dictionary where the key is a last name and the value is a list of first names.
# The function should return a new dictionary where each key is the first letter of a last name,
# and the value is the number of people whose last name begins with that letter.


def count_first_letter(names):
    letters = {}
    for key in names:
        first_letter = key[0]
        if first_letter not in letters:
            letters[first_letter] = 0
        letters[first_letter] += len(names[key])
    return letters


print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Twn"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Sannister": ["Jaime", "Cersei", "Twn"]}))
