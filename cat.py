class Cat():
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

    def speak(self):
        return "Meow"  


stella = Cat()
stella.name = "Stella"
stella.age = 7
word = stella.speak()
stella.speak()

garfield = Cat()
garfield.name = "Garfield"
garfield.age = 50
sound = garfield.speak()
garfield.speak()

print(word + sound)