pattern = open('str1.txt','r').read().strip()
genome = open('str2.txt','r').read().strip()
d = 2
position = []

def approx_pat(pattern, genome, d):
    for i in range (len(genome) - len(pattern)+1):
        if hamming_distance(pattern, genome[i:i + len(pattern)]) <= int(d):
            position.append(i)
    return position

def hamming_distance(q, p):
        dist = 0
        for i in range(len(p)):
            if p[i] != q[i]:
                dist += 1
        return dist

#print(*approx_pat(pattern, genome, d))


y = (approx_pat(pattern, genome, d))
print (len(y))

#y = [13,20,303,45]

#The answer to this question will be

#print (len(y))
