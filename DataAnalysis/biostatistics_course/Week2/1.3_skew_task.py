genome = open('dataset.txt','r').read()
def Skew(genome):
    Skew = {}

    Skew[0] = 0
    for i in range(1, len(genome)+1):
        if genome[i - 1] == "G":
            Skew[i] = Skew[i - 1] + 1
        elif genome[i - 1] == "C":
            Skew[i] = Skew[i - 1] - 1
        else:
            Skew[i] = Skew[i-1]
    return Skew


def MinimumSkew(genome):

    positions = [] # output variable
    s = Skew(genome)
    m = min(s.values())
    for (k,v) in s.items():
        if v == m:
            positions.append(k)
    return positions
#print(MinimumSkew(genome))



numList = MinimumSkew(genome)
#print ('\n'.join(map(str, numList)))
print (' '.join(map(str, numList)))
