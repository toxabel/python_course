import re
import csv
from collections import Counter


# define function that read data from current txt file
def read_csv_file():
     with open('message_column.txt', 'r') as txtfile:
          txt_data = txtfile.read()
     return txt_data


# define function that create words report
def words_report():
     # get string with lowercase words
     almost_words = re.sub("[^A-Za-z]", " ", read_csv_file()).lower()

     # splits the string into words and puts it in a list without spaces
     list_almost_words = almost_words.split(" ")
     list_words = list(filter(None, list_almost_words))

     # count how many times words occurs in a string and put the results into a dictionary
     unique_words = Counter(list_words)

     # iterate over all key-values from a dictionary and write them to a CSV document
     for key, values in unique_words.items():
          with open('words_report.csv', 'a', newline='') as csvfile:
               writer = csv.writer(csvfile, delimiter='-')
               writer.writerow([key, values])

     print('Words report ready')


# define function that create letters report
def letters_report():
     # get string with all letters as is and string with all letters in lowercase
     origin_letters = re.sub("[^A-Za-z]", "", read_csv_file())
     all_letters_lower = re.sub("[^A-Za-z]", "", read_csv_file()).lower()

     # count how many times letters occur in strings and put the results into dictionaries
     dict_origin_letters = Counter(origin_letters)
     dict_all_letters_lower = Counter(all_letters_lower)

     # call the context manager and define the parameters for writing data to a CSV document
     with open('letters_report.csv', 'a', newline='') as csvfilel:
          columns_names = ['letter', 'count_all', 'count_uppercase', 'percentage']
          writer = csv.DictWriter(csvfilel, fieldnames=columns_names)
          writer.writeheader()

          # iterate over all key-values from a dictionaries
          for key, values in dict_all_letters_lower.items():
               for key_origin, values_origin in dict_origin_letters.items():

                    # count the percentage of each letter in data string
                    letter_rate = round(values / len(all_letters_lower) * 100, 1)

                    # condition for those letters that occur in upper and lower case
                    if key == key_origin and values != values_origin:
                         writer.writerow({'letter': key, 'count_all': values,\
                                          'count_uppercase': (values - values_origin),'percentage': letter_rate})
                    # condition for those letters that occur lower case only
                    elif key == key_origin and values == values_origin:
                         writer.writerow({'letter': key, 'count_all': values,\
                                          'count_uppercase': 0, 'percentage': letter_rate})

     print('Letters report ready')
