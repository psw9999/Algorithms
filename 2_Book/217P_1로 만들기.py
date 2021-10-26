
# 책 풀이와 비교.. 책 풀이가 엄청 간단함.
d = [0] * 30001

n = int(input())

for i in range(1,n+1) :
    if d[i+1] == 0 :
        d[i+1] = d[i]+1
    
    else :
        if d[i+1] > d[i]+1 :
            d[i+1] = d[i]+1 
    
    if d[i*2] == 0 :
        d[i*2] = d[i] + 1
    else :
        if d[i*2] > d[i] + 1 :
            d[i*2] = d[i] + 1

    if d[i*3] == 0 :
        d[i*3] = d[i] + 1
    else :
        if d[i*3] > d[i] + 1 :
            d[i*3] = d[i] + 1

    if d[i*5] == 0 :
            d[i*5] = d[i] + 1
    else :
        if d[i*5] > d[i] + 1 :
            d[i*5] = d[i] + 1

print(d[n])

    
    