from Sphynx import Sphynx

yourSphynxName = input('name:')
yourSphynxColor = input('color:')
s = Sphynx(yourSphynxName, yourSphynxColor)
print(s.name, s.color)
