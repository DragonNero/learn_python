counts = dict()
names = ['dragon', 'popka', 'bar', 'truth','cat', 'dragon']
for name in names :
    counts[name] = counts.get(name, 0) +1
    #print(name, ':', counts[name])
for cat,number, dog in counts.items():
    print(cat,'->', number, dog)

print(counts)
