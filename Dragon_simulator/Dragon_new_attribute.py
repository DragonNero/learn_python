from Sphynx import Sphynx
hunger = 0
thirst = 0
yourSphynxName = input('name:')
yourSphynxColor = input('color:')
sphynxHunger = hunger + 1
sphynxThirst = thirst + 1
s = Sphynx(yourSphynxName, yourSphynxColor, sphynxHunger, sphynxThirst)
print(s.name, s.color, s.hunger, s.thirst)
