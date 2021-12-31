
T,W = map(int, input().split())

jadu = [int(input()) for _ in range(T)]

arr = [[0] * (T+1) for _ in range(W+1)]

for i in range(0, W+1) :
    for j in range(1,T+1) :
        if i % 2 == 1 :
            if jadu[j-1] == 2 :
                arr[i][j] = max(arr[i-1][j]+1, arr[i][j-1]+1)
            else :
                arr[i][j] = arr[i][j-1]
        else :
            if jadu[j-1] == 1 :
                arr[i][j] = max(arr[i-1][j]+1, arr[i][j-1]+1)
            else :
                arr[i][j] = arr[i][j-1]

print(max(arr[W][T],arr[W-2][T]))
    
for a in arr :
    print(a)