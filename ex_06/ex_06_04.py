text = "X-DSPAM-Confidence:    0.8475";

#print(text)
find = text.find(':')
#print(find)
piece = text[find+2:]
#print(piece)
value = float(piece)
print(value)
#print(value+43)
