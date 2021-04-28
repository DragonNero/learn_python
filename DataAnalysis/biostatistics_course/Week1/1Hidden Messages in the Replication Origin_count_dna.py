text = input('Enter text: ')
pattern = input('Enter pattern: ')
text_length = len(text)
pattern_length = len(pattern)
count = 0
for i in range(text_length - pattern_length+1):
    if text[i:i+pattern_length] == pattern:
        count = count + 1
print("Number of pattern frequency:", count)
