# import os and orchestrator modules
import os
import orchestrator

if __name__ == '__main__':
    # get input by the user from input console
    message_source = int(input("Choose message source: 1 - Manual input, 2 - Txt as source \nYour variant: "))

    # call function from the orchestrator module to process manual input
    if message_source == 1:
        orchestrator.parse_manual_input()

    # call function from the orchestrator module to process txt file parsing and delete this file in the end
    elif message_source == 2:
        print(orchestrator.parse_txt_file())

        if os.path.exists("input.txt"):
            os.remove("input.txt")
        else:
            print("The file does not exist")
