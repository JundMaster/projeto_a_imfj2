from floating import *

over = False
userInput = ""

while (not over):
    print("What problem do you want to solve?")
    print("1. Floating")
    print("2. Springs")
    userInput = input(">")
    if (userInput == "1"):
        FloatingLoop()
    elif (userInput.lower() == "exit"):
        print("Bye bye!")
        break