def mismatches_and_rc(text,k,d):
    frequencyarray={}
    rev_text=rev_comp(text)
    for i in range(0,4**k):
        frequencyarray[i]=0
    for i in frequencyarray:
        count,r_count=0,0
        count=PatternMatching(text,NumberToPattern(i,k),d)
        r_count=PatternMatching(rev_text,NumberToPattern(i,k),d)
        frequencyarray[i]=count+r_count
    return frequencyarray


def PatternMatching(text,pat,d):
    count=0
    for i in range(0,len(text)):
        p=text[i:i+len(pat)]
        if len(p)!= len(pat): break
        if hammingdistance(p,pat)<=d:
            count=count+1
    return count

def PatternToNumber(pattern):
    if len(pattern)==0: return
    SymbolToNumber = {'A':0,'C':1,'G':2,'T':3}
    if len(pattern)==1: return SymbolToNumber[pattern]
    n=len(pattern)
    symbol=pattern[n-1]
    prefix=pattern[:n-1]
    return (4*PatternToNumber(prefix)+SymbolToNumber[symbol])

def NumberToPattern(index,k):
    NumberToSymbol = {0:'A',1:'C',2:'G',3:'T'}
    if k==1: return NumberToSymbol[index]
    prefix_index=index//4
    r=index%4
    symbol=NumberToSymbol[r]
    return NumberToPattern(prefix_index,k-1)+symbol

def hammingdistance(p,q):
    count=0
    if len(p)!= len(q):
        print("The two sequences vary in lenghts")
        return
    for i in range(0,len(p)):
        if p[i]!=q[i]:
            count=count+1
    return count

def rev_comp(pattern):
    rpattern=''
    a=[]
    for i in pattern:
        if i=='A':
            a.append('T')
        if i=='T':
            a.append('A')
        if i=='C':
            a.append('G')
        if i=='G':
            a.append('C')
    rpattern =rpattern.join(a)
    return(rpattern[::-1])


text=input('Enter the text')
k=int(input('Enter length of k-mer'))
d=int(input('Enter d'))
approx_kmers= mismatches_and_rc(text,k,d)
for a in approx_kmers:
    if approx_kmers[a]== max(approx_kmers.values()):
        print(NumberToPattern(a,k),end=' ')
