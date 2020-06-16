from floating import *
from spring import *

over = False
userInput = ""

while (not over):
    print("What problem do you want to solve?")
    print("1. Floating")
    print("2. Springs")

    # Gets user input
    userInput = input(">")
    if (userInput == "1"):
        print("\n" * 2)
        # Goes to floatation problem resolution
        FloatingLoop()

    elif (userInput == "2"):
        print("\n" * 2)
        # Goes to string problem resolution
        SpringLoop()
        
    elif (userInput.lower() == "exit"):
        print("Bye bye!")
        exit()
    else:
        print(f"'{userInput}' is not a valid option.")
        print("Choose 1 or 2.")
        print("If you mean to quit, use the command 'exit'")
        input("\nPress Enter to continue...")
    print("\n" * 3) 
