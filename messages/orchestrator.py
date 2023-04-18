# import publication and parser_txt modules
import publication
import parser_txt
import parser_json
import parser_xml
import json
import xml.etree.ElementTree as ET


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


# define function that parses text from json file
def parse_json_file():
    # opening the json file and read data
    with open('json_input.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

        # put data into the list of dicts
        list_dict = (json_data['messages'])

    # parse text in each dict from list dicts according to the type of news
    for message_dict in list_dict:
        for key, value in message_dict.items():
            if key == 'name' and value == 'Joke':
                joke_json = parser_json.JokeJSON(message_dict)
                joke_json.publish_txt()
            elif key == 'name' and value == 'News':
                joke_json = parser_json.NewsJSON(message_dict)
                joke_json.publish_txt()
            elif key == 'name' and value == 'Ad':
                joke_json = parser_json.AdJSON(message_dict)
                joke_json.publish_txt()

    return 'File JSON successfully processed'


def parse_xml_file():
    # parse the xml file, read data and get xml root
    xml_data = ET.parse('xml_input.xml')
    root = xml_data.getroot()

    # parse elements from xml tree according to the type of news
    for message_element in root.iter('MESSAGE'):
        if message_element.attrib['name'] == "Joke":
            joke_xml = parser_xml.JokeXML(message_element)
            joke_xml.publish_txt()
        elif message_element.attrib['name'] == "News":
            news_xml = parser_xml.NewsXML(message_element)
            news_xml.publish_txt()
        elif message_element.attrib['name'] == "Ad":
            ad_xml = parser_xml.AdXML(message_element)
            ad_xml.publish_txt()

    return 'File XML successfully processed'
