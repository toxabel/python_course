hw_string = r"""homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

standart_string = hw_string.capitalize()

print(standart_string)

print(hw_string.count(' '))

cnt = 0
for i in hw_string:
    if i.isspace() == True:
        cnt = cnt + 1

print(cnt)
