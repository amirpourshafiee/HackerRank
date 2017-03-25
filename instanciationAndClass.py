class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge <0:
            print("Age is not valid, setting age to 0.")
            self.Age=0
        else:
            self.Age=initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if (self.Age > 17):
            print("You are old.")
        elif (self.Age<13):
            print("You are young.")
        else:
            print("You are a teenager.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.Age +=1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
