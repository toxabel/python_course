# import the re module
import re

# define list
list_of_words = []

# variable with homework string
hw_string = r"""homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# define function that return number of whitespace characters in current text
def number_whitespace(text_string):
    # initialize a variable with defined value = 0
    num_spaces = 0
    # loop through all the characters in the text sting
    for i in text_string:
        # check if the symbol is space if yes add 1 to variable
        if i.isspace() == True:
            num_spaces = num_spaces + 1
    return num_spaces

# print number of whitespace
print("Number of whitespace characters:", number_whitespace(hw_string))


# fix spelling mistakes
# find all the words "iz" using regular expressions and replace them with "is" in a homework paragraph
hw_with_correct_is = re.sub(r"(?i)iz\b", 'is', hw_string)


# normalized text from letter cases point of view
# define function that return string after method 'capitalize'
def normalize(match_str):
    return match_str.group().capitalize()

# find sentences in a homework paragraph using regular expressions and replace them with new versions
# obtained after method 'capitalize' from function normalize
hw_normalized = re.sub(r"[A-Z|a-z][^\.!?:]*[\.!?:]", normalize, hw_with_correct_is)


# creating a new sentence from the last words and add it to the end of this paragraph
# find the last word in each sentence in a homework paragraph using regular expressions and add them to list
list_of_words = re.findall(r"(\w+[^\d|])[\.!?:]", hw_normalized)

# define function that convert list to string
def listToString(list_of_words):
    # initialize an empty string
    new_sentence = " "
    # return string contains a new sentence generated from the list of words
    return (new_sentence.join(list_of_words)+".")

# print normalized homework sentence with new sentence generated from the last words
print(hw_normalized + " " + listToString(list_of_words))