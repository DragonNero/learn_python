fhand = open('text_test.txt', 'r')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
            print(line)
