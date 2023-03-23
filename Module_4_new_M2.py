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


# defain function that create list of dictionaries with random values and keys is letters in lowercase
def dictionries_list(dictionary_number, key_value_number, top_value_range):
    # create list of dictionaries from 1 to dictionary_number
    for d in range(1, dictionary_number):
        # create a dictionary with random key-value pair from 1 to 9
        for kv in range(1, key_value_number):
            # get random letter in lowercase as key and assign number from 1 to 100 as value
            random_dict[random.choice(string.ascii_lowercase)] = random.randint(1, top_value_range)
        #print("random_dict: ", random_dict)
        # add copy of generated random dictionary into list of dictionary
        list_dicts.append(random_dict.copy())
    return list_dicts

# call function dictionries_list and print list of dictionary with kay-values
print("list_dicts", dictionries_list(10, 10, 100))


def fill_dictionary(dictionary_name):
    # loop through all the dictionaries from the list
    for dict_items in list_dicts:
        # loop through all key-value from the current dictionary from a list of dictionaries
        for key, value in dict_items.items():
            # if dictionary name is index_dict
            if dictionary_name == index_dict:
                # add new key-value item or and new value for existing key in dictionary
                dictionary_name[key].append(list_dicts.index(dict_items))
            # else if dictionary name is values_dict
            elif dictionary_name == values_dict:
                # add new key-value item or and new value for existing key in dictionary
                dictionary_name[key].append(value)
    return dictionary_name

# call function fill_dictionary with parameter and print results
print("Dictionary with indexes: ", fill_dictionary(index_dict), '\n', "Dictionary with values: ", fill_dictionary(values_dict))


# define function that return dictionary with max values for each key and correct key name
def get_result_dict():
    # loop through all items of dictionary with values
    for key, values in values_dict.items():
        # loop through all items of dictionary with indexes
        for index_key, index_values in index_dict.items():
            # if the keys from values_dict and index_dict match and number of values from values_dict = 1
            if key == index_key and len(values) == 1:
                # call function add_key_value with parameters
                result_dict.update({key: max(values)})
            # else if the keys from values_dict and index_dict match and number of values from values_dict > 1
            elif key == index_key and len(values) > 1:
                # get real index for max values for each key
                value_index = values.index(max(values))
                # call function add_key_value with parameters
                result_dict.update({key + str('_') + str(index_values[value_index] + 1): max(values)})
    return result_dict

# call function get_result_dict and print dictionary with result
print("result_dict: ", get_result_dict())