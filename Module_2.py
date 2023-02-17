# import the random module
import random


# define dicts and list
random_dict = {}
list_dicts = []
alphabet_dict = {}
mid_res_dict = {}
result_dict = {}


# create list of dictionarys (from 2 to 10) with random values (1-100) and keys is letters in lowercase
for d in range(2, 11):
    # get a number from 1 to 13 which will be a step in the next random function
    r_step = random.randint(1, 14)
    # create a dictionary with random key-value pair from 2 to 26
    for kv in range(1, 27, r_step):
        # get a number from 1 to 100 which will be a value of
        r_value = random.randint(1, 101)
        # get letter in lowercase
        random_dict[chr(kv+96)] = r_value
    # print generated random dictionary
    print("random_dict: ", random_dict)
    # add copy of generated random dictionary into list of dictionary
    list_dicts.append(random_dict.copy())


# define a number of dictionaries contains in a list
len_ld = len(list_dicts)


# create a dictionary with lowercase letters in alphabet order with defined values 0
for l in range(1, 27):
    alphabet_dict[chr(l+96)] = 0


# update values in dictionary with letters, value contains the number of identical keys in all dictionaries of the list
for ad_key, ad_value in alphabet_dict.items():
    # loop through all the dictionaries from the list
    for u in range(0, len_ld):
        # loop through all key-value from the current dictionary from a list of dictionaries
        for key, value in list_dicts[u].items():
            # if the keys from the alphabet dictionary and the current dictionary match
            if ad_key == key:
                # add an increment to the value and update the value for the matched key in the alphabet dictionary
                ad_value = ad_value + 1
                alphabet_dict[key] = ad_value
            else:
                pass
# print list of dictionarys
print("list_dicts", list_dicts)


# get a dictionary with max values for each key, and add to the key number with a dictionary with a max value
for adv_key, adv_value in alphabet_dict.items():
    # if the key occurs once in the list of dictionaries
    if adv_value == 1:
        # loop through all the dictionaries from the list
        for i in range(0, len_ld):
            # loop through all key-value from the current dictionary from a list of dictionaries
            for key, value in list_dicts[i].items():
                # if the keys from the alphabet dictionary and the current dictionary match
                if adv_key == key:
                    # add key-value pair into result dictionary
                    result_dict[key] = value
    # else if the key occurs more than once in the list of dictionaries
    elif adv_value > 1:
        # loop through all the dictionaries from the list
        for i in range(0, len_ld):
            # loop through all key-value from the current dictionary from a list of dictionaries
            for key, value in list_dicts[i].items():
                # if the keys from the alphabet dictionary and the current dictionary match
                if adv_key == key:
                    # generate a new key name (old key name + "_" + number of the current dictionary)
                    gen_key = str(key) + "_" + str(i + 1)
                    # add key-value pair into intermediate result dictionary
                    mid_res_dict[gen_key] = value

        # get max value from intermediate result dictionary
        max_value = max(mid_res_dict.values())

        # list out keys-value pairs separately
        key_list = list(mid_res_dict.keys())
        val_list = list(mid_res_dict.values())

        # get position of max value
        position = val_list.index(max_value)
        # get the first key name according to the position of max value
        get_key = key_list[position]

        # add key-value pair with first key name with max value into result dictionary
        result_dict[get_key] = max_value
        # clear intermediate result dictionary
        mid_res_dict.clear()
    else:
        pass

# print dictionary with result
print("result_dict: ", result_dict)
