# Dict = set of key:value pairs


# adding a key:
my_dict["new key"] = "new value"

# adding multiple keys:
my_dict.update({"new key": "new value", "new key 2": "new value 2"})

# overwrite values:
my_dict["old key"] = "new value"

# list comprehension to dict:

list1 = [1, 2, 3]
list2 = ["one", "two", "three"]

dict_from_both_lists = {key: value for key, value in zip(list1, list2)}



# check if key exists 1 way:

key_to_check = "sth"
if key_to_check in my_dict:
    print(my_dict["sth"])


# check if key exists try/except way:

key_to_check = "sth"
try:
    print(my_dict[key_to_check])
except KeyError:
    print("that key doesn't exist")


# check if key exists get() method:

my_dict.get("sth")
my_dict.get("sth", "no value")


# delete a key

new_dict = my_dict.pop("sth")

# get all keys:

users = user_ids.keys()

# get all values:

total = []
for sth in num_ex.values():
    total += sth


# get all items ---> tuple

my_dict.items()

for key, value in my_dict.items():
    print(f"somethin {value} something else {key}")
