text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
k_num = 3

def FrequentWords(text, k_num):

    k_mer_dic ={}

    for i in range(len(text)-k_num+1):

        word = text[i:i+k_num]

        if word not in k_mer_dic:
            k_mer_dic[word] = 1
        else:
            k_mer_dic[word]+=1

    k_mer_list=[]
    max_num = max([x for x in k_mer_dic.values()])
    for key, value in k_mer_dic.items():
        if value == max_num:
            k_mer_list.append(key)

    print(k_mer_list)
    return k_mer_list

FrequentWords(text, k_num)
