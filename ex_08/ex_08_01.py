numList = list()
while True :
    inp = input('Enter a number: ')
    inp = inp.lower()
    if inp == 'done': break
    value = float(inp)
    numList.append(value)

average = sum(numList) / len(numList)
print('Average ', average)
