# import the random module
import random


# define 3 lists
numbs = []
numbs_even = []
numbs_odd = []


# create list of 100 random numbers from 0 to 1000 inclusive
for i in range(100):
    # generate random numbers and add than on by one to the end of a "numbs" list
    numbs.append(random.randint(0, 1001))


# sort list from min to max
# get the number of list elements
n = len(numbs)

# traverse through all list elements as many times as the length of the list -1,
# because penultimate time we will set two elements in place
for i in range(n - 1):
    # traverse the each list elements from 0 to n-1-i
    for j in range(n - 1 - i):
        # check if element (number) from list is greater than next one
        if numbs[j] > numbs[j + 1]:
            # swap the elements of list
            numbs[j], numbs[j + 1] = numbs[j + 1], numbs[j]


# filter each elements from "numbs" list to even and odd lists
for n in numbs:
    # if the fractional part of number after division by 2 is zero add number in "numbs_even" list
    if n % 2 == 0:
        numbs_even.append(n)
    # else this number is odd and necessary to add in "numbs_odd" list
    else:
        numbs_odd.append(n)


# calculate and print average values from lists: numbs_even, numbs_odd
print("Average value from EVEN list is:", sum(numbs_even)/len(numbs_even))
print("Average value from  ODD list is:", sum(numbs_odd)/len(numbs_odd))