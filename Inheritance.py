# Dry : Dont Repeat yourself
# Class Dog dan Cat Meng-inheritkan isinya ke class Mammal

class Mammal :
    def walk(self):
        print("walk")


class Dog(Mammal):
    # Pass berarti tidak ada, ibaratkan kita mengatakan ke python interpreter untuk melewatkan baris ini
    def bark(self):
        print('Bark')


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()


