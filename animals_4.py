class Cat:

    def __init__(self):
        self.mood = 'neutral'

    def speak(self):
        if self.mood == 'happy':
            print("Purr")
        elif self.mood == 'angry':
            print('Hiss!')
        else:
            print("Meow!")

class Dog:
    scientific_name = 'Canis lupus familiaris'

    def __init__(self, name):
        self.name = name
        self.woofs = 1

    def bark(self):
        pass


    def count(self):
        for bark in range(self.woofs):
            self.speak()
        self.woofs += 1

    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == 'biscuit':
            print('Yummy!')
        else:
            print('That is not food!')

    def hear(self, words):
        if self.name in words:
            self.speak()

class Chihuahua(Dog):
    origin = "Mexico"

    def speak(self):
        print("Yep!")

class Husky(Dog):
    origin = "Siberia"

    def speak(self):
        print("Awoooo!")

    def bark(self):
        print("Awooooooooooooooooo!")
