class NinjaClass:
    def __init__(self, first_name, last_name, treats, pet_food, pet,noise):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        self.health = 100
        self.energy =50
        self.noise = noise
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bath(self):
        self.pet.noise()
ninja=NinjaClass("fuma","jinishi","treat grain","chicky","ninja hund")
        
class PetClass:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
    def sleep(self):
        self.energy+=25
        return self
    def eat(self):
        self.energy+=5
        self.health+=10
        return self
    def play(self):
        self.health+=5
        self.energy-=15
        return energy
    def noise(self):
        print(self.noise)
my_treats=['Sausage','becon',"trash bag"]
my_pet_food=["pizza","burger"]
houndi=pet()
    