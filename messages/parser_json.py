from datetime import date, timedelta
import publication
import normalization


# define child class JokeJSON that publish jokes in document from JSON file
class JokeJSON(publication.Joke):
    # class constructor and class attribute
    def __init__(self, message_dict):
        publication.Joke.__init__(self, message_dict)
        self.text_dict = message_dict

    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
        message_name = normalization.normalize(self.text_dict['name'])
        message_text = normalization.normalize(self.text_dict['text'])

        content = "\n" + message_name + "\n" + message_text + "\n"
        return content


# define child class NewsJSON that publish news in document from JSON file
class NewsJSON(JokeJSON):
    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
        current_date = date.today()
        message_name = normalization.normalize(self.text_dict['name'])
        message_text = normalization.normalize(self.text_dict['text'])
        message_city = normalization.normalize(self.text_dict['city'])

        content = "\n" + message_name + "\n" + message_text + "\n" + message_city + ", " + str(current_date) + "\n"
        return content


# define child class AdJSON that publish Ads in document from JSON file
class AdJSON(JokeJSON):
    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
        current_date = date.today()
        message_name = normalization.normalize(self.text_dict['name'])
        message_text = normalization.normalize(self.text_dict['text'])
        message_availability = int(self.text_dict['availability'])

        end_date = current_date + timedelta(days=message_availability)

        content = "\n" + message_name + "\n" + message_text + "\n" + "Actual until: " + str(end_date) + ", " + \
                  str(message_availability) + " days left" + "\n"
        return content
