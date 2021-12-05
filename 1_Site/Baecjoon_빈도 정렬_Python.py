
N,C = map(int,input().split())

dic = {}

in_list = list(map(int, input().split()))

for i in in_list :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1

dic = sorted(dic.items(), key = lambda item : item[1], reverse = True)

for i, j in dic :
    for z in range(j) :
        print(i, end= " ")