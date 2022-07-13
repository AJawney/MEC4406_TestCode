# Print name:
print("Yenwaj Werdna")

# Count to favorite number squared:
favNum = 15
Numsqrd = favNum**2

for i in range(0,Numsqrd+1):
    print(i)

# Declare object:
class Engineers:
    def __init__(self,Name,Field,Years):
        self.Name = Name
        self.Field = Field
        self.Years = str(Years)
        self.Skill = "problem solver"

# Create objects (Engineers)
eng1 = Engineers("Andrew", "Mechatronic", 5)
eng2 = Engineers("Brian", "Agricultural", 7)

# Print out Engineer attributes:
print(vars(eng1))
print(vars(eng2))
