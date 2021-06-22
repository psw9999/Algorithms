
# 내가 짠 코드
# 틀린 방식은 아니나 if(k > n)이 while 안에 있어서 루프를 한번 돌때마다 비교를 한번씩 더해야함.
# 그러므로 저 조건식을 바깥쪽으로 빼는 것이 더 효율적이다.
# n,k = map(int,input().split())

# result = 0

# while(1) :
#     if n==1 :
#         break
#     if(k > n) :
#         result += (n-1)
#         break
#     else :
#         temp = n % k
#         result += (temp + 1) # 1로 뺀 횟수(temp) + 나눴으므로 1을 더함.
#         n = (n//k)
1
# print(result)

# 다시 짠 방식
n,k = map(int,input().split())

result = 0

while(k <= n) :
    temp = n % k
    result += (temp + 1) # 1로 뺀 횟수(temp) + 나눴으므로 1을 더함.
    n = (n//k)

result += (n-1)
print(result)