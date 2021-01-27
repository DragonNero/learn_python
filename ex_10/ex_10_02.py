d = {'c':22, 'b':1, 'a':10}
t = list(d.items())
#print(t)
t.sort()
#print(t)

for key, val in d.items() :
    t.sort(reverse=True)
    print(key,val)
