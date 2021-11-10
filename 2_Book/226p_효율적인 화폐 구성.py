n,m = list(map(int,input().split()))

money = []
da = [m+1] * (m+1)

for i in range(n) :
    money.append(int(input()))
    if money[i] < m+1 :
        da[money[i]] = 1

for i in range(len(da)) :
    if da[i] == m+1 :
        continue
    
    else :
        for j in money :
            if i+j < m+1 :
                da[i+j] = min(da[i+j], da[i]+1)

if da[m] == m+1 :
    print(-1)
else :
    print(da[m])