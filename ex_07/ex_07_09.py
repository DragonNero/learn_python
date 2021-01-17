
fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be open: ', fname)
    quit()
count = 0
value = 0

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    text = line.find(':')
    piece = line[text+2:]
    #print(piece)

    value = value + float(piece)#print(value)




avg = value/count
print("Average spam confidence", avg)
