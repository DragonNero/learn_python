import re
hand = open('regex_sum_1122012.txt')
print(hand)
numList = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0: continue
    for num in stuff:
        num = int(num)
        numList.append(num)

    print(stuff)
total = sum(numList)
print(total)
