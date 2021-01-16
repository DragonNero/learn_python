fhand = open('text_test.txt', 'r')
for line in fhand:
    line = line.rstrip()
    if not 'From' in line:
        continue
    print(line)
