# import os and orchestrator modules
import os
import orchestrator
import report_csv

if __name__ == '__main__':
    # get input by the user from input console
    message_source = int(input("Choose message source:   1 - Manual input,   2 - TXT as source file,\
   3 - JSON as source file,   4 - XML as source file \nYour variant: "))

    # call function from the orchestrator module to process manual input
    if message_source == 1:
        orchestrator.parse_manual_input()

    # call function from the orchestrator module to process txt file parsing, delete this file in the end
    elif message_source == 2:
        print(orchestrator.parse_txt_file())

        os.remove("input.txt")

    # call function from the orchestrator module to process JSON file parsing, delete this file in the end
    elif message_source == 3:
        print(orchestrator.parse_json_file())

        os.remove("json_input.json")

    # call function from the orchestrator module to process XML file parsing, delete this file in the end
    elif message_source == 4:
        print(orchestrator.parse_xml_file())

        os.remove("xml_input.xml")

    # call reports functions from the report_csv module
    report_csv.words_report()
    report_csv.letters_report()
