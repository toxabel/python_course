# Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format
#
# You need to implement:
# 1.News – text and city as input. Date is calculated during publishing.
# 2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.
#
# Each new record should be added to the end of file. Commit file in git for review.

from datetime import date


class MainMessage:
    def __init__(self):
        pass

    def message_type(self):

        user_variant = input("Choose message type: 1 - Joke, 2 - News, 3 - Ad \nYour variant: ")

        o = Orchestrator(user_variant)
        o.executor()


class Orchestrator:
    def __init__(self, user_variant):
        self.uv = user_variant

    def executor(self):
        if self.uv == str(1):
            user_text = self.text()
            j = Joke("Joke", user_text)
            j.save_message_name()
            j.save_message()
        elif self.uv == str(2):
            user_text = self.text()
            n = News("News", user_text)
            n.save_message_name()
            n.save_message()
            n.save_date()
        elif self.uv == str(3):
            pass

    def text(self):
        user_text = input("Your Text: ")
        return user_text


class Joke:
    def __init__(self, message_name, user_text):
        self.ut = user_text
        self.mn = message_name

    def save_message_name(self):
        with open('message_column.txt', 'a') as f:
            f.write("\n" + self.mn)

    def save_message(self):
        with open('message_column.txt', 'a') as f:
            f.write("\n" + self.ut + "\n")


class News(Joke):
    def save_date(self):
        carent_date = date.today()
        with open('message_column.txt', 'a') as f:
            f.write(str(carent_date) + "\n")

class Ad(News):
    pass

b = MainMessage
b.message_type(0)
