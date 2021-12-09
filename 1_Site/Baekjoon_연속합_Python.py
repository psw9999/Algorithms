
N = int(input())

array = list(map(int,input().split()))

cur,Vmax = array[0], array[0]

for i in range(1, N) :
    if cur + array[i] < 0 :
        if cur < 0 :
            cur = max(cur+array[i],array[i])
        else :
            cur = 0
    else :
        cur = cur + array[i]
    Vmax = max(Vmax, cur)

print(Vmax)

## 다른사람 풀이 : 더 깔끔함
# def find_max(arr, num):
#     if num == 0:
#         return 0
#     tot = arr[0]
#     max_tot = tot
#     for i in range(1, num):
#         if tot > 0 and tot + arr[i] >= 0:
#             tot += arr[i]
#         else:
#             tot = arr[i]
#         if max_tot < tot:
#             max_tot = tot
#     return max_tot