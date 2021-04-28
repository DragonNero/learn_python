punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

inp_str = open('string_to_clean.txt','r').read()

no_punc = ""
for char in inp_str:
   if char not in punctuations:
       no_punc = no_punc + char

print("Punctuation Free String: ",no_punc)
