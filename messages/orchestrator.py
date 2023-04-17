# import publication and parser_txt modules
import publication
import parser_txt


# define function that parses manual input in console
def parse_manual_input():
    # get input by the user from input console
    user_variant = int(input("Choose message type: 1 - Joke, 2 - News, 3 - Ad \nYour variant: "))

    # define methode that create objects of various classes by condition
    if user_variant == 1:
        joke = publication.Joke("Joke")
        joke.publish_txt()
    elif user_variant == 2:
        news = publication.News("News")
        news.publish_txt()
    elif user_variant == 3:
        news = publication.Ad("Ad")
        news.publish_txt()


# define function that parses text from txt file
def parse_txt_file():
    # opening the file and read data
    with open("input.txt", "r") as txtfile:
        data = txtfile.read()

    # splitting the text it further when '\n' is seen.
    list_data = data.split('\n')

    # parse each lines from list_data according to the type of news
    for line in list_data:
        if line.startswith("Joke"):
            joke_txt = parser_txt.JokeTxt(line)
            joke_txt.publish_txt()
        elif line.startswith('News'):
            news_txt = parser_txt.NewsTxt(line)
            news_txt.publish_txt()
        elif line.startswith('Ad'):
            ad_txt = parser_txt.AdTxt(line)
            ad_txt.publish_txt()

    return 'File txt successfully processed'
