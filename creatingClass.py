class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name + " is barking....")

    def waddle(self):
        print(self.name + " is wagging his talil")


rex = Dog('rex', 'pitbull')
killa = Dog('killa', 'German Shepherd')
rex.bark()
rex.waddle()
print('-------------------')
print(rex.name.capitalize() + ' is a' + ' ' + rex.breed)
print(killa.name.capitalize() + ' is a' + ' ' + killa.breed)
