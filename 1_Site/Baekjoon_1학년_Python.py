
N = int(input())

arr = list(map(int,input().split()))
result = 0

DP = [0] * 21

DP[arr[0]] = 1

for i in range(1, len(arr)-1) :
    tempDP = [0] * 21
    for j in range(len(DP)) :
        if DP[j] > 0 :
            if arr[i] == 0 :
                tempDP[j] = DP[j] * 2
            else :
                temp_1 = j + arr[i]
                temp_2 = j - arr[i]
                if temp_1 <= 20 :
                    tempDP[temp_1] += DP[j]
                if temp_2 >= 0 :
                    tempDP[temp_2] += DP[j]
                DP[j] = 0
    DP = tempDP
    print(arr[i], DP)

print(DP[arr[N-1]])
                