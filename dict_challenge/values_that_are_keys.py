# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter.
# This function should return a list of all values in the dictionary that are also keys.


def values_that_are_keys(my_dict):
    values_that_are_keys = []
    for value in my_dict.values():
        if value in my_dict.keys():
            values_that_are_keys.append(value)
    return values_that_are_keys


print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
