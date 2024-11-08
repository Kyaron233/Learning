class animal:
    def __init__(self, name):
        self.name = name
    def soar(self):
        print(self.name+" soaring!")

cat = animal("cat")
cat.soar()

class dog(animal):
    def __init__(self):
        self.name = "dog"
        print("<child method \"dog\" called>")
    def soar(self):
        print("woof! woof!")

dog = dog()
dog.soar()

class Cat(animal):
    def __init__(self):
        self.name = "cat"
        print("<child method \"Cat\" called>")
    def soar(self):
        print("meow! meow!")

cat = Cat()
cat.soar()
