# import the date, timedelta and normalization modules
from datetime import date, timedelta
import normalization


# define parent class Joke that publish jokes in document
class Joke:
    # class constructor and class attribute
    def __init__(self, message_name):
        self.name = message_name

    # define method that get message text from user by input console
    def text(self):
        user_text = normalization.normalize(input("Your Text: "))
        return user_text

    # define method that prepares message content in one variable
    def prepare_content(self):
        content = "\n" + self.name + "\n" + self.text() + "\n"
        return content

    # define method that publish message content by adding text to the end of the txt document
    def publish_txt(self):
        to_publish = self.prepare_content()
        with open('message_column.txt', 'a') as f:
            f.write(to_publish)


# define child class News that publish news in document
class News(Joke):

    # define method that gets city name from user by input console
    def get_city_name(self):
        user_city = normalization.normalize(input("Your City Location: "))
        return user_city

    # override method that prepares message content in one variable according to the template
    def prepare_content(self):
        current_date = date.today()
        content = "\n" + self.name + "\n" + self.text() + "\n" + str(self.get_city_name()) + ", " + str(
            current_date) + "\n"
        return content


# define child class Ad that publish user advertisement in document
class Ad(Joke):

    # define method that gets number of days that Ad will be available from user by input console
    def day_number(self):
        user_days_number = input("Specify how many days the Ad will be available: ")
        return user_days_number

    # override the method that prepares the content of the message in one variable
    def prepare_content(self):
        current_date = date.today()
        days_number = int(self.day_number())
        end_date = current_date + timedelta(days=days_number)
        content = "\n" + self.name + "\n" + self.text() + "\n" + "Actual until: " + str(end_date) + ", " \
                  + str(days_number) + " days left" + "\n"
        return content
