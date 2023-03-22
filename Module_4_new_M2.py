# import the random, string and collections modules
import random
import string
import collections

# define dicts and list
random_dict = {}
list_dicts = []
result_dict = {}

# define empty defaultdict objects that can contain items with key-list of values
index_dict = collections.defaultdict(list)
values_dict = collections.defaultdict(list)


# define a function that returns lowercase letters
def low_case():
    return string.ascii_lowercase

# create list of dictionaries (from 2 to 10) with random values (1-100) and keys is letters in lowercase
for d in range(2, 10):
    # create a dictionary with random key-value pair from 1 to 9
    for kv in range(1, 10):
        # get random letter in lowercase from low_case function as key and assign number from 1 to 100 as value
        random_dict[random.choice(low_case())] = random.randint(1, 101)
    # print generated random dictionary
    print("random_dict: ", random_dict)
    # add copy of generated random dictionary into list of dictionary
    list_dicts.append(random_dict.copy())
# print list of dictionaries
print("list_dicts", list_dicts)


# define a function that add new key-value item or and new value for existing key in dictionary
def append_value(dict_name, dict_key, dict_value):
    return dict_name[dict_key].append(dict_value)

# get defaultdict object with each key and list with dictionaries indexes that contain value of that key
# loop through all the dictionaries from the list
for dict_items in list_dicts:
    # loop through all key-value from the current dictionary from a list of dictionaries
    for key, value in dict_items.items():
        # call function append_value with parameters
        append_value(index_dict, key, (list_dicts.index(dict_items)))
# print dictionary with indexes of value for each unique key
print('index_dict:', index_dict)


# get defaultdict object with each key and list of values from each of dictionaries
# loop through all the dictionaries from the list
for dict_items in list_dicts:
    # loop through all key-value from the current dictionary from a list of dictionaries
    for key, value in dict_items.items():
        # call function append_value with parameters
        append_value(values_dict, key, value)
# print dictionary with values for each unique key
print('values_dict:', values_dict)


# add key-value in to preassigned dictionary
def add_key_value(dict_name, dict_key, dict_value):
    return dict_name.update({dict_key: dict_value})

# get max values for each key and form the correct key name
# loop through all items of dictionary with values
for key, values in values_dict.items():
    # loop through all items of dictionary with indexes
    for index_key, index_values in index_dict.items():
        # if the keys from values_dict and index_dict match and number of values from values_dict = 1
        if key == index_key and len(values) == 1:
            # call function add_key_value with parameters
            add_key_value(result_dict, key, max(values))
        # else if the keys from values_dict and index_dict match and number of values from values_dict > 1
        elif key == index_key and len(values) > 1:
            # get real index for max values for each key
            value_index = values.index(max(values))
            # call function add_key_value with parameters
            add_key_value(result_dict, key + str('_') + str(index_values[value_index] + 1), max(values))

# print dictionary with result
print("result_dict: ", result_dict)