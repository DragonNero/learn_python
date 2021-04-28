lst = open('string_to_clean.txt','r').read()
print("List before adding newline character to it:",lst)
lst = '\n'.join(lst)
print("List after adding newline character to it:\n",lst)
