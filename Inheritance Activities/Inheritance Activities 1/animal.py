class Animal:
    def __init__(self, name):
        self._name = name  

    def get_sound(self):
        print("This animal makes a sound, but it's not defined.")

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name) 
        self._sound = sound     

    def get_sound(self):
        super().get_sound()
        print(self._name + " the dog says: " + self._sound)

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name)  
        self._sound = sound    

    def get_sound(self):
        super().get_sound()  
        print(self._name + " the cat says: " + self._sound)


dog1 = Dog("Rex", "Woof")
cat1 = Cat("Mittens", "Meow")

dog1.get_sound()
cat1.get_sound()
