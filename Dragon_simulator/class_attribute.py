class Attribute:
    name = ''
    value = 0

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def increase(self, amount):
        if amount < 0:
            print('amount must be positive')
            exit()
        self.value += amount
        if self.value > 100:
             self.value = 100

    def decrease(self, amount):
        if amount < 0:
            print('amount must be positive')
            exit()
        self.value -= amount
        if self.value < -100:
            self.value = -100

a = Attribute("hunger", 4)
print(a.name, a.value)
a.decrease(-108)
print('Decrement of', a.name, a.value)
