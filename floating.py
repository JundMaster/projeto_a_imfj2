class Float():
    def __init__(self, gravity, mass, volume, fluidDensity, objectDensity):
        self.gravity        = gravity
        self.mass           = mass
        self.volume         = volume
        self.fluidDensity   = fluidDensity
        self.objectDensity  = objectDensity
        self.c              = 0
        self.center         = 0

    def Recalculate(self):
        gravityForce    = self.mass * self.gravity
        imersedVolume   = gravityForce/(self.gravity * self.fluidDensity)
        side            = self.volume **(1/3)
        self.c          = imersedVolume/(side * side)
        self.center     = -(self.c  - side * 0.5)

    def SetVolume(self, volumeValue):
        self.volume = volumeValue
        self.mass   = self.volume * self.objectDensity
    
    def SetGravity(self, gravityValue):
        self.gravity = gravityValue
    
    def SetMass(self, massValue):
        self.mass   = massValue
        self.volume = self.mass / self.objectDensity

    def SetFluidDensity(self, fluidDensityValue):
        self.fluidDensity = fluidDensityValue
    
    def SetObjectDensity(self, objectDensityValue):
        self.objectDensity  = objectDensityValue
        self.mass           = self.objectDensity * self.volume


over = False
userInput = ""

def FloatingHelp():
    print("FloatingHelp")


floatingObj = Float(9.81, 121.05, 0.12, 1000, 450)

def FloatingLoop():
    while (not over):

        print("Object properties:")
        print(f"Mass = {floatingObj.mass}")
        print(f"Fluid Density = {floatingObj.fluidDensity}")
        print(f"Object Density = {floatingObj.objectDensity}")
        print(f"Object Volume = {floatingObj.volume}")
        print(f"Gravity = {floatingObj.gravity}")
        print(f"\nObject would float at: {floatingObj.center}")

        userInput = input(">")
        user_choice = []
        user_choice = userInput.split(' ')

        if(user_choice[0].lower() == "set"):

            if (user_choice[1].lower() == "mass" and len(user_choice) == 3):
                mass = user_choice[2]
                floatingObj.SetMass((float)(mass))

            elif (user_choice[1].lower() == "volume" and len(user_choice) == 3):
                volume = user_choice[2]
                floatingObj.SetVolume((float)(volume))

            elif (user_choice[1].lower() == "fluid" and user_choice[2].lower() == "density" and len(user_choice) == 4):
                fluidDensity = user_choice[3]
                floatingObj.SetFluidDensity((float)(fluidDensity))

            elif (user_choice[1].lower() == "gravity" and len(user_choice) == 3):
                gravity = user_choice[2]
                floatingObj.SetGravity((float)(gravity))

            elif (user_choice[1].lower() == "object" and user_choice[2].lower() == "density" and len(user_choice) == 4):
                objectDensity = user_choice[3]
                floatingObj.SetObjectDensity((float)(objectDensity))

        if (user_choice[0].lower() == "exit"):
            print("Bye Bye!")
            exit()



        floatingObj.Recalculate()