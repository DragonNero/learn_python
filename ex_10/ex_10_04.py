fhand = open('mbox-short.txt')
timeList = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    #guardian
    if len(words) < 3 or words[0] != 'From' :
        continue
    timeExploded = words[5].split(':')
    hours = timeExploded[0]
    timeList[hours] = timeList.get(hours,0) +1

for key in sorted(timeList):
    print(key, timeList[key])
