import re
hand = open('mbox-short.txt')
numList = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) !=1: continue
    num = float(stuff[0])
    numList.append(num)
print('Maximum:', max(numList))
