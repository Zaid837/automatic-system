class Mammal:
    blood="warm"
    limbs= 4
    eyes= 2

class Dog(Mammal):
    family = "Canine"

class Cat(Mammal):
    family= "Feline"

bob = Cat()
bruno = Dog()
generic = Mammal()

print(bob.family)
print(bob.blood)
print(bruno.family)
print(generic.family)
