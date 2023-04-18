from datetime import date, timedelta
import publication
import normalization


# define child class JokeXML that publish jokes in document from XML file
class JokeXML(publication.Joke):
    # class constructor and class attribute
    def __init__(self, message_element):
        publication.Joke.__init__(self, message_element)
        self.xml_element = message_element

    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
        message_name = 'Joke'
        message_text = normalization.normalize(self.xml_element.find('TEXT').text)

        content = "\n" + message_name + "\n" + message_text + "\n"
        return content


# define child class NewsXML that publish news in document from XML file
class NewsXML(JokeXML):
    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
        current_date = date.today()
        message_name = 'News'
        message_text = normalization.normalize(self.xml_element.find('TEXT').text)
        message_city = normalization.normalize(self.xml_element.find('CITY').text)

        content = "\n" + message_name + "\n" + message_text + "\n" + message_city + ", " + str(current_date) + "\n"
        return content


# define child class AdXML that publish Ads in document from XML file
class AdXML(JokeXML):
    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
            current_date = date.today()
            message_name = 'Ad'
            message_text = normalization.normalize(self.xml_element.find('TEXT').text)
            message_availability = int(self.xml_element.find('AVAILABILITY').text)

            end_date = current_date + timedelta(days=message_availability)

            content = "\n" + message_name + "\n" + message_text + "\n" + "Actual until: " + str(end_date) + ", " + \
                      str(message_availability) + " days left" + "\n"
            return content
