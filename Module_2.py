# import the random module
import random


# define
l1 = {}
numbs = []
numbs_even = []
numbs_odd = []

# create list of dicts with random values (1-100) and keys is letters
#l1 = dict.fromkeys([chr(j):j for j in range(65, 90)])


for i in range(1, 27):
    j = random.randint(1, 101)
    l1[chr(i+96)] = j

print(l1)


# create list of 100 random numbers from 0 to 1000 inclusive
for i in range(100):
    # generate random numbers and add than on by one to the end of a "numbs" list
    numbs.append(random.randint(0, 1001))

# sort list
numbs.sort()

