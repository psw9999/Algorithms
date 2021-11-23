tc = int(input())

for _ in range(tc) :
    n = int(input())
    d = {}
    for i in range(n) :
        name, kind = input().split()
        if kind in d :
            d[kind] += 1
        else :
            d[kind] = 1
    result = 1
    # for j in d.values() :
    #     result *= (j+1)
    for key in d :
        result *= (d[key] + 1)
    print(result-1)