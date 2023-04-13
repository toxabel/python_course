# import the date and timedelta modules
from datetime import date, timedelta

# define main class that start conversation with user
class MainMessage:
    # class constructor
    def __init__(self):
        pass

    # define method that gets type of message from user, creates an object of the class and calls its method "executor"
    def message_type(self):

        # get user's answer and save it in variable "user variant"
        user_variant = input("Choose message type: 1 - Joke, 2 - News, 3 - Ad \nYour variant: ")

        # creates an object of the class and calls its method "executor"
        o = Orchestrator(user_variant)
        o.executor()

# define class that creates objects of various classes and runs the appropriate methods according to the user's choice
class Orchestrator:
    # class constructor and class attribute
    def __init__(self, user_variant):
        self.uv = user_variant

    # define methode that create objects of various classes by condition
    def executor(self):
        if self.uv == str(1):
            j = Joke("Joke")
            j.publish_txt()
        elif self.uv == str(2):
            n = News("News")
            n.publish_txt()
        elif self.uv == str(3):
            a = Ad("Ad")
            a.publish_txt()


# define parent class Joke that publish jokes in document
class Joke:
    # class constructor and class attribute
    def __init__(self, message_name):
        self.mn = message_name

    # define method that get message text from user by input console
    def text(self):
        user_text = input("Your Text: ")
        return user_text

    # define method that prepares message content in one variable
    def prepare_content(self):
        content = "\n" + self.mn + "\n" + self.text() + "\n"
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
        user_city = input("Your City Location: ")
        return user_city

    # override method that prepares message content in one variable according to the template for news messages
    def prepare_content(self):
        carrent_date = date.today()
        content = "\n" + self.mn + "\n" + self.text() + "\n" + str(self.get_city_name()) + ", " + str(carrent_date) + "\n"
        return content

# define child class Ad that publish user advertisement in document
class Ad(Joke):

    # define method that gets number of days that Ad will be available from user by input console
    def day_number(self):
        user_days_number = input("Specify how many days the Ad will be available: ")
        return user_days_number

    # override the method that prepares the content of the message in one variable
    def prepare_content(self):
        carrent_date = date.today()
        days_number = int(self.day_number())
        end_date = carrent_date + timedelta(days=days_number)
        content = "\n" + self.mn + "\n" + self.text() + "\n" + "Actual until: " + str(end_date) + ", " \
                  + str(days_number) + " days left" + "\n"
        return content

# creates object of the  main class and calls method "message_type" that start conversation with user
b = MainMessage
b.message_type(0)