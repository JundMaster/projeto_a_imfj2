class Spring():
    def __init__(self, spring_constant, base_len, object_mass, gravity):
        self.spring_constant    = spring_constant
        self.object_mass        = object_mass
        self.gravity            = gravity
        self.base_len           = base_len
        self.stretched_len      = 0.0

    def Recalculate(self):
        gravity_force = (self.object_mass * self.gravity) * -1
        self.stretched_len = ((self.spring_constant * self.base_len) - gravity_force) / (self.spring_constant)
    
    def SetGravity(self, gravity_value):
        self.gravity = gravity_value

    def SetMass(self, mass_value):
        self.object_mass = mass_value
    
    def SetBaseLength(self, length_value):
        self.base_len = length_value
    
    def SetSpringConstant(self, constant_value):
        self.spring_constant = constant_value


def SpringHelp():
    print("\nset mass <T>:          changes the object current mass value to T.")
    print("set gravity <T>:         changes the current gravity value to T.")
    print("set base length <T>:     changes the spring current base length value to T.")
    print("set spring constant <T>: changes the current spring constant value to T.")
    input("\nPress Enter to continue...")
    print("\n" * 2)

def SpringIndicator():
    print(" "+"_" * 60)
    print("|" + " " * 60 + "|")
    print("|{:{align}{width}}|".format("S P R I N G", align="^", width="60"))
    print("|" + "_" * 60 + "|")


spring_obj = Spring(25, 0.25, 0.5, 9.81)
spring_obj.Recalculate()

def SpringLoop():
    over = False
    userInput = ""
    invalid_value = "\n\033[91m" + "I N V A L I D    V A L U E" + "\033[0m"
    while (not over):
        error = False
        SpringIndicator()
        print("Properties:")
        print(f"Gravity: {round(spring_obj.gravity, 2)} m/s²")
        print(f"Object mass: {round(spring_obj.object_mass, 2)} kg")
        print(f"Spring constant: {round(spring_obj.spring_constant, 2)} N/m")
        print(f"Spring base length: {round(spring_obj.base_len, 2)} m")
        print(f"\nSpring would stretch to {spring_obj.stretched_len} m.")

        # Gets user input
        userInput = input(">")
        user_choice = []

        # Splits user input into the user_choice arra
        user_choice = userInput.split(' ')

        # Checks if the user used the command set
        if(user_choice[0].lower() == "set"):
            # Checks if user input was meant to set a new mass value
            if (user_choice[1].lower() == "mass" and len(user_choice) == 3):
                mass = 0
                try:
                    mass = (float)(user_choice[2])
                except:
                    error = True
                # If inserted mass is 0 or less, it prints an error message
                if (mass <= 0.0):
                    print(invalid_value)
                    if (error):
                        print("Please insert a number, not a string.")
                    else:
                        print("Please chose a mass value greater then 0.")
                    input("Press Enter to continue...")
                    print("\n" * 3)
                    continue
                # Sets object mass to the inserted value
                spring_obj.SetMass(mass)

            # Checks if user input was meant to set a new gravity value
            if (user_choice[1].lower() == "gravity" and len(user_choice) == 3):
                gravity = 0
                try:
                    gravity = (float)(user_choice[2])
                except:
                    error = True
                # If inserted gravity is 0 or less, it prints an error message
                if (gravity <= 0.0):
                    print(invalid_value)
                    if (error):
                        print("Please insert a number, not a string.")
                    else:
                        print("Please chose a gravity value greater then 0.")
                    input("Press Enter to continue...")
                    print("\n" * 3)
                    continue
                # Sets gravity to the inserted value
                spring_obj.SetGravity(gravity)

            # Checks if user input was meant to set a new base length value
            elif (user_choice[1].lower() == "base" and user_choice[2].lower() == "length" and len(user_choice) == 4):
                try:
                    base_length = (float)(user_choice[3])
                except:
                    error = True
                # If inserted base length is 0 or less, it prints an error message
                if (base_length <= 0.0):
                    print(invalid_value)
                    if (error):
                        print("Please insert a number, not a string.")
                    else:
                        print("Please chose a base length value greater then 0.")
                    input("Press Enter to continue...")
                    print("\n" * 3)
                    continue
                # Sets base length to the inserted value
                spring_obj.SetBaseLength(base_length)

            # Checks if user input was meant to set a new spring constant value
            elif (user_choice[1].lower() == "spring" and user_choice[2].lower() == "constant" and len(user_choice) == 4):
                constant = 0
                try:
                    constant = (float)(user_choice[3])
                except:
                    error = True
                # If inserted spring constant is 0 or less, it prints an error message
                if (constant <= 0.0):
                    print(invalid_value)
                    if (error):
                        print("Please insert a number, not a string.")
                    else:
                        print("Please chose a spring constant value greater then 0.")
                    input("Press Enter to continue...")
                    print("\n" * 3)
                    continue
                # Sets spring constant to the inserted value
                spring_obj.SetSpringConstant(constant)

        # Checks if the user used the command 'exit'
        if (user_choice[0].lower() == "exit"):
            print("Bye Bye!\n")
            exit()

        # Checks if the user used the command 'back'
        elif (user_choice[0].lower() == "back"):
            print("\n" * 2)
            break

        # Checks if the user used the command 'help'
        elif (user_choice[0].lower() == "help"):
            # Prints list of commands
            SpringHelp()
        # Checks if the user input doesn't match any of the valid commands
        else:
            print(f"\n'{userInput}' is not a valid command.")
            print("Use the command 'help' to get a list of valid commands.")
            input("\nPress Enter to continue...")

        print("\n" * 3)
        spring_obj.Recalculate()