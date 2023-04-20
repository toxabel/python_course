# import pyodbc module
import pyodbc


# define parent class PublishIntoDb that publishes messages into DB according to type of messages
class PublishIntoDb:
    # class constructor, class attributes, and open connection to db with creation cursor
    def __init__(self, name, create_table, check_elem, insert_elem):
        self.name = name
        self.to_create = create_table
        self.to_check = check_elem
        self.to_insert = insert_elem
        with pyodbc.connect(f"DRIVER={{SQLite3 ODBC Driver}};Database={self.name}.db", autocommit=True) as self.connection:
            self.cursor = self.connection.cursor()

    # define method that creates table, make validation of existing element in DB and insert element into DB
    def publish_message(self):
        # create table if not exists
        self.cursor.execute(f'{self.to_create}')

        # check if exists message in table of DB and if not insert it into
        self.cursor.execute(f"{self.to_check}")
        if str(self.cursor.fetchone()) == '(\'false\',)':
            print('This record already exists')
        else:
            self.cursor.execute(f"{self.to_insert}")
            print('Record inserted in DB successfully ')

        # print all rows from current table
        self.cursor.execute(f'SELECT * FROM {self.name}')
        print(self.cursor.fetchall())
