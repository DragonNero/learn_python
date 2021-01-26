fhand = open('mbox-short.txt')
emailList = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    #guardian
    if len(words) < 3 or words[0] != 'From' :
        continue
    #print(words[1])
    emailList[words[1]] = emailList.get(words[1],0) +1
    #emailList.append(words[1])
#print(emailList)
#print(len(emailList))
#print("There were", len(emailList), "lines in the file with From as the first word")

#print(emailList)

bigcount = None
bigword = None
for email,count in emailList.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count

print(bigword, bigcount)
