class Attribute:
    name = ''
    value = 0

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def increase(self, amount):
        self.value += amount

    #def decrease(self):
        #return self.hunger -= 1

a = Attribute("hunger", 4)
print(a.name, a.value)
a.increase(30)
print('Increment of', a.name, a.value)
