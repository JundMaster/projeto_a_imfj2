over = False
userInput = ""

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
        print(f"boraaaa {self.c}")

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

def FloatingHelp():
    print("FloatingHelp")


gravity         = 9.81
mass            = 121.05
volume          = 0.12
fluidDensity    = 1000
gravityForce    = mass * gravity
testVolume      = gravityForce/(gravity * fluidDensity)
side            = testVolume**(1/3)
c               = testVolume/(side * side)


floatingObj = Float(9.81, 121.05, 0.12, 1000, 450)
while (not over):

    userInput = input(">")

    if (userInput.lower() == "set mass"):
        mass = input("Insert a mass value: ")
        floatingObj.SetMass((float)(mass))

    elif (userInput.lower() == "set volume"):
        volume = input("Insert a volume value: ")
        floatingObj.SetVolume((float)(volume))

    elif (userInput.lower() == "set fluid density"):
        fluidDensity = input("Insert a fluid density value: ")
        floatingObj.SetFluidDensity((float)(fluidDensity))

    elif (userInput.lower() == "set gravity"):
        gravity = input("Insert a gravity value: ")
        floatingObj.SetGravity((float)(gravity))

    elif (userInput.lower() == "set object density"):
        objectDensity = input("Insert a object density value: ")
        floatingObj.SetObjectDensity((float)(objectDensity))



    floatingObj.Recalculate()
    print(f"Object properties:")
    print(f"Mass = {floatingObj.mass}")
    print(f"Fluid Density = {floatingObj.fluidDensity}")
    print(f"Object Density = {floatingObj.objectDensity}")
    print(f"Volume = {floatingObj.volume}")
    print(f"Gravity = {floatingObj.gravity}")
    print(f"\nObject would float at: {floatingObj.center}")