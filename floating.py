class Float():
    def __init__(self, gravity, mass, volume, fluid_density, object_density):
        self.gravity        = gravity
        self.mass           = mass
        self.volume         = volume
        self.fluid_density   = fluid_density
        self.object_density  = object_density
        self.c              = 0
        self.center         = 0

    def Recalculate(self):
        gravity_force    = self.mass * self.gravity
        immersed_volume   = gravity_force/(self.gravity * self.fluid_density)
        side            = self.volume **(1/3)
        self.c          = immersed_volume/(side * side)
        self.center     = side * 0.5 - self.c

    def SetVolume(self, volume_value):
        self.volume = volume_value
        self.mass   = self.volume * self.object_density
    
    def SetGravity(self, gravity_value):
        self.gravity = gravity_value
    
    def SetMass(self, mass_value):
        self.mass   = mass_value
        self.volume = self.mass / self.object_density

    def SetFluidDensity(self, fluid_density_value):
        self.fluid_density = fluid_density_value
    
    def SetObjectDensity(self, object_density_value):
        self.object_density  = object_density_value
        self.mass           = self.object_density * self.volume

def FloatingHelp():
    print("\nset mass <T>:            changes the object current mass value to T.")
    print("set gravity <T>:         changes the current gravity value to T.")
    print("set volume <T>:          changes the object current volume value to T.")
    print("set fluid density <T>:   changes the object current fluid density value to T.")
    print("set object density <T>:  changes the object current object density value to T.")
    input("\nPress Enter to continue...")
    print("\n" * 2)

def FloatingIndicator():
    print(" "+"_" * 60)
    print("|"+ "\033[94m"  +" ‿" + "︵‿" * 7 + "F L O A T I N G" + "︵‿" * 7 + "\033[0m" + " |")
    print("|"+ "\033[94m"  + "︵‿" * 20 +"\033[0m" +"|")
    print("|" + "_" * 60 + "|")

floating_obj = Float(9.81, 121.05, 0.12, 1000, 450)
floating_obj.Recalculate()  

def FloatingLoop():
    over = False
    userInput = ""
    invalid_value = "\n\033[91m" + "I N V A L I D    V A L U E" + "\033[0m"
    while (not over):
        error = False
        FloatingIndicator()
        print("Object properties:")
        print(f"Fluid Density = {floating_obj.fluid_density} Kg/m³")
        print(f"Mass = {floating_obj.mass} Kg")
        print(f"Object Density = {floating_obj.object_density} Kg/m³")
        print(f"Object Volume = {floating_obj.volume} m³")
        print(f"Gravity = {floating_obj.gravity} m²")
        print(f"\nObject would float at: {floating_obj.center} m")

        # Gets user input
        userInput = input(">")
        user_choice = []

        # Splits user input into the user_choice array
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
                floating_obj.SetMass(mass)

            # Checks if user input was meant to set a new volume value
            elif (user_choice[1].lower() == "volume" and len(user_choice) == 3):
                volume = 0
                try:
                    volume = (float)(user_choice[2])
                except:
                    error = True
                # If inserted volume is 0 or less, it prints an error message
                if (volume <= 0.0):
                    print(invalid_value)
                    if (error):
                        print("Please insert a number, not a string.")
                    else:
                        print("Please chose a volume value greater then 0.")
                    input("Press Enter to continue...")
                    print("\n" * 3) 
                    continue
                # Sets object volume to the inserted value
                floating_obj.SetVolume(volume)

            # Checks if user input was meant to set a new fluid density value
            elif (user_choice[1].lower() == "fluid" and user_choice[2].lower() == "density" and len(user_choice) == 4):
                fluid_density = 0
                try:
                    fluid_density = (float)(user_choice[3])
                except:
                    error = True
                # If inserted fluid density is 0 or less, it prints an error message
                if (fluid_density <= 0.0):
                    print(invalid_value)
                    if (error):
                        print("Please insert a number, not a string.")
                    else:
                        print("Please chose a fluid density value greater then 0.")
                    input("Press Enter to continue...")
                    print("\n" * 3) 
                    continue
                # Sets fluid density to the inserted value
                floating_obj.SetFluidDensity(fluid_density)

            # Checks if user input was meant to set a new gravity value
            elif (user_choice[1].lower() == "gravity" and len(user_choice) == 3):
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
                floating_obj.SetGravity(gravity)

            # Checks if user input was meant to set a new object density value
            elif (user_choice[1].lower() == "object" and user_choice[2].lower() == "density" and len(user_choice) == 4):
                object_density = 0
                try:
                    object_density = (float)(user_choice[3])
                except:
                    error = True
                # If inserted object density is 0 or less, it prints an error message
                if (object_density <= 0.0):
                    print(invalid_value)
                    if (error):
                        print("Please insert a number, not a string.")
                    else:
                        print("Please chose a object density value greater then 0.")
                    input("Press Enter to continue...")
                    print("\n" * 3) 
                    continue
                # Sets object density to the inserted value
                floating_obj.SetObjectDensity(object_density)

        # Checks if the user used the command 'exit'
        elif (user_choice[0].lower() == "exit"):
            print("Bye Bye!\n")
            exit()

        # Checks if the user used the command 'back'
        elif (user_choice[0].lower() == "back"):
            print("\n" * 2)
            break

        # Checks if the user used the command 'help'
        elif (user_choice[0].lower() == "help"):
            # Prints list of commands
            FloatingHelp()
        # Checks if the user input doesn't match any of the valid commands
        else:
            print("\033[91m" + f"'{userInput}' is not a valid command." + "\033[0m")
            print("\033[91m" + "pudim" + "\033[0m")
            print("Use the command 'help' to get a list of valid commands.")
            input("\nPress Enter to continue...")

        print("\n" * 3)
        floating_obj.Recalculate()