#helpful in creating variations in classes
class Doggo:
    species = "Canis familiaris" # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says"
        f"{sound}"
    
class Labrador(Doggo):
    def speak(self, sound):
        return "Hello"
#Instantiating Various instances of Doggod
miles = Doggo("Miles", 4)
buddy = Doggo("Buddy", 9)
jack = Doggo("Jack", 3)
jim = Doggo("Jim", 5)

buddy.speak("Yap")
jim.speak("Woof")
jack.speak("Woof")