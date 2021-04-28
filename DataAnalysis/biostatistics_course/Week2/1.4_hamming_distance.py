#genome = open('dataset.txt','r').read()



#numList = MinimumSkew(genome)
#print ('\n'.join(map(str, numList)))
#print (' '.join(map(str, numList)))
def hammingDist(str1, str2):
    i = 0
    count = 0

    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count

# Driver code
#str1 = "GGGCCGTTGGT"
str1 = open('str1.txt','r').read()
#str2 = "GGACCGTTGAC"
str2 = open('str2.txt','r').read()
# function call
print(hammingDist(str1, str2))
