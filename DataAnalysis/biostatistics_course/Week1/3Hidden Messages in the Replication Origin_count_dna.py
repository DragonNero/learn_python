Text = ('AAAACCCGGT')
def ReverseComp(Text):
    b=""
    for i in range(len(Text)):
        if Text[i] == 'A':
            a="T"
        elif Text[i] =='C':
            a="G"
        elif Text[i] =='T':
            a="A"
        elif Text[i] =='G':
            a="C"
        b=a+b
    comp=b
    return comp
