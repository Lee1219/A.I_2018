import math

def Training():
    text, d_text = load_Data("ratings_train.txt")
    tokens = []
    labels = []

    for d in d_text:
        t = d[1].split()
        if t != 0:
            tokens.append(t)
        else:
            exit(-1)
        labels.append(int(d[2]))

    f=open("ratings_train.txt",'r', encoding='UTF8')
    g=open("ratings_train_result.txt", 'w', encoding='UTF8')
    pos_cnt = 0
    neg_cnt = 0
    doc_list = dict()

    for i in range(len(labels)):
        if labels[i]==1:
            pos_cnt += len(tokens[i])
        else :
            neg_cnt += len(tokens[i])

    for i in range(len(tokens)):
        for t in tokens[i]:
            if t !="":
                if t in doc_list:
                    tmp = doc_list[t]
                    if labels[i]==1:
                        tmp[0]+=1
                    else:
                        tmp[1]+=1
                    doc_list[t]=tmp
                else:
                    if labels[i]==1:
                        doc_list[t] = [1,0]
                    else:
                        doc_list[t] = [0,1]

    str_info = (str(pos_cnt), "\t", str(neg_cnt), "\t", str(pos_cnt + neg_cnt), "\n")
    g.writelines(str_info)

    for d in doc_list:
        str_d = (d, "\t", str(doc_list[d][0]), "\t", str(doc_list[d][1]), "\n")
        g.writelines(str_d)
    return 0

def load_Training(fileName):
    f = open(fileName, 'r', encoding='UTF8')

    str = f.readline()
    str = str.replace("\n","")
    str= str.split("\t")

    pos_cnt = str[0]
    neg_cnt = str[1]

    text = []
    for line in f.readlines():
        text.append(line.strip('\n'))

    d_text = {}
    for t in text:
        info = t.split('\t')
        d_text[info[0]] = [int(info[1]), int(info[2])]

    return int(pos_cnt), int(neg_cnt), d_text

def load_Data(fileName):
    f=open(fileName,'r',encoding='UTF8')
    text=[]
    d_text=[]
    idx = f.readline()
    for line in f.readlines():
        text.append(line.strip('\n'))
    for txt in text:
        d_text.append(txt.split('\t'))

    return text, d_text

def classification(text, DB, toks, pos_cnt, neg_cnt):
    cnt = pos_cnt + neg_cnt
    prob_p = -math.log(pos_cnt/cnt)
    prob_n = -math.log(neg_cnt/cnt)
    pr_p = prob_p
    pr_n = prob_n

    f=open("ratings_result.txt","w", encoding='UTF8')
    str_info=("id","\t","document","\t","label","\n")
    f.writelines(str_info)

    for i in range(len(toks)):
        for t in toks[i]:
            if t in DB:
                p = DB[t]
                if p[0] == 1:
                    prob_p -= - math.log(p[0] / pos_cnt)
                else:
                    prob_p += 1000000
                if p[1] == 1:
                    prob_n -= math.log(p[1] / neg_cnt)
                else:
                    prob_n += 1000000
            else:
                prob_p -= math.log(0.5)
                prob_n -= math.log(0.5)

        if pr_p <= pr_n:
            if prob_p < prob_n:
                str = (text[i], "\t", '1', "\n")
                f.writelines(str)
            else:
                str = (text[i], "\t", '0', "\n")
                f.writelines(str)
        else:
            if prob_p <= prob_n:
                str = (text[i], "\t", '1', "\n")
                f.writelines(str)
            else:
                str = (text[i], "\t", '0', "\n")
                f.writelines(str)
            prob_p = pr_p
            prob_n = pr_n

def main():
    while True:
        c = int(input("<<Operation you can choose>> \n 1. Training \n 2. Classification \n Press number what you want to do : "))

        if c == 1:
            Training()
            print("Training Completed!")

        elif c == 2:
            text, d_text = load_Data("ratings_test.txt")
            tok=[]
            if d_text != 0:
                for d in d_text:
                    t = d[1].split()
                    if t != 0:
                        tok.append(t)
                    else:
                        exit(-1)

                pos_cnt, neg_cnt, DB = load_Training("ratings_train_result.txt")
                classification(text, DB, tok, pos_cnt, neg_cnt)
                print("classification completed!\n")
        else :
            print("You've pressed Wrong Number")
if __name__ == '__main__':
    main()
