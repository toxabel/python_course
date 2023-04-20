# import publish_into_db module
import publish_into_db


# define function that parses published_text with message/s, prepare parameters according to type of message/s
# and runs method publish_message of instance class PublishIntoDb
def split_text(published_text):
    name = published_text.split('\n')[1]
    text = published_text.split('\n')[2]
    if name.startswith("Joke"):
        to_create = f'CREATE TABLE IF NOT EXISTS {name} (name TEXT, text TEXT)'
        to_check = f'SELECT CASE WHEN COUNT(*) > 0 THEN \'false\' ELSE \'true\' END FROM {name} WHERE name == \'{name}\' and text == \'{text}\''
        to_insert = f"INSERT INTO {name} VALUES ('{name}', '{text}')"
        publish_db = publish_into_db.PublishIntoDb(name, to_create, to_check, to_insert)
        publish_db.publish_message()
    elif name.startswith("News"):
        third_line = published_text.split('\n')[3]
        city = third_line.split(',')[0]
        data = third_line.split(',')[1]
        to_create = f'CREATE TABLE IF NOT EXISTS {name} (name TEXT, text TEXT, city TEXT, data DATE)'
        to_check = f'SELECT CASE WHEN COUNT(*) > 0 THEN \'false\' ELSE \'true\' END FROM {name} WHERE name == \'{name}\' and text == \'{text}\' and city == \'{city}\' and data == \'{data}\''
        to_insert = f"INSERT INTO {name} VALUES ('{name}', '{text}', '{city}' , '{data}')"
        publish_db = publish_into_db.PublishIntoDb(name, to_create, to_check, to_insert)
        publish_db.publish_message()
    elif name.startswith("Ad"):
        third_line = published_text.split('\n')[3]
        deadline = third_line.split(',')[0]
        availability = third_line.split(',')[1]
        to_create = f'CREATE TABLE IF NOT EXISTS {name} (name TEXT, text TEXT, deadline TEXT, availability TEXT)'
        to_check = f'SELECT CASE WHEN COUNT(*) > 0 THEN \'false\' ELSE \'true\' END FROM {name} WHERE name == \'{name}\' and text == \'{text}\' and deadline == \'{deadline}\' and availability == \'{availability}\''
        to_insert = f"INSERT INTO {name} VALUES ('{name}', '{text}', '{deadline}' , '{availability}')"
        publish_db = publish_into_db.PublishIntoDb(name, to_create, to_check, to_insert)
        publish_db.publish_message()
