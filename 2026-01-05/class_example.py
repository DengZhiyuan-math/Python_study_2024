class PartyAnimal:
    def __init__(self, z):
        self.x = 0
        self.mingzi = z
        print(self.mingzi, "is constructed with", self.x)
    def party(self):
        self.x = self.x +1
        print(self.mingzi, "party count", self.x)

    def __del__(self):
        print("The class is deconstructed", self.x)

s = PartyAnimal("S")


s.party()
s.party()
s.party()

s = 42
print(s)