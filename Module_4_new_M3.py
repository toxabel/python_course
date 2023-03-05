import re

list_of_words = []

hw_string = r"""homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# number of whitespace characters
cnt = 0
for i in hw_string:
    if i.isspace() == True:
        cnt = cnt + 1
print("Number of whitespace characters:", cnt)


# fix spelling mistakes
hw_with_correct_is = re.sub(r"(?i)iz\b", 'is', hw_string)
#print(hw_with_correct_is)


# normalized text from letter cases point of view
def normalize(match_str):
    return match_str.group().capitalize()

hw_normalized = re.sub(r"[A-Z|a-z][^\.!?:]*[\.!?:]", normalize, hw_string)
print(hw_normalized)


# creating a new sentence from the last words
list_of_words = re.findall(r"\w+[^\d|][\.!?:]", hw_normalized)
print(list_of_words)