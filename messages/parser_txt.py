# import the date, timedelta, publication and normalization modules
from datetime import date, timedelta
import publication
import normalization


# define child class JokeTxt that publish jokes in document from txt file
class JokeTxt(publication.Joke):
    # class constructor and class attribute
    def __init__(self, message_line):
        publication.Joke.__init__(self, message_line)
        self.text_line = normalization.normalize(message_line)

    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
        message_name = self.text_line.split('|')[0]
        message_text = normalization.normalize(self.text_line.split('|')[1])

        content = "\n" + message_name + "\n" + message_text + "\n"
        return content

# define child class NewsTxt that publish news in document from txt file
class NewsTxt(JokeTxt):
    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
        current_date = date.today()
        message_name = self.text_line.split('|')[0]
        message_text = normalization.normalize(self.text_line.split('|')[1])
        message_city = normalization.normalize(self.text_line.split('|')[2])

        content = "\n" + message_name + "\n" + message_text + "\n" + message_city + ", " + str(current_date) + "\n"
        return content


# define child class AdTxt that publish Ads in document from txt file
class AdTxt(JokeTxt):
    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
        current_date = date.today()
        message_name = self.text_line.split('|')[0]
        message_text = normalization.normalize(self.text_line.split('|')[1])
        message_availability = int(self.text_line.split('|')[2])

        end_date = current_date + timedelta(days=message_availability)

        content = "\n" + message_name + "\n" + message_text + "\n" + "Actual until: " + str(end_date) + ", " + \
                  str(message_availability) + " days left" + "\n"
        return content
