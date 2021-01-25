fhand = open('romeo.txt')
wordList = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()


    for word in words:
        if word in wordList: continue
        wordList.append(word)
wordList = sorted(wordList)

print(wordList)
    #if len(words) < 1 or words[0] != 'From' :
        #continue
    #print(words)
