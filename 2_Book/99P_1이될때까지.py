n,k = map(int,input().split())

result = 0

while(k <= n) :
    temp = n % k
    result += (temp + 1) # 1로 뺀 횟수(temp) + 나눴으므로 1을 더함.
    n = (n//k)

result += (n-1)
print(result)
