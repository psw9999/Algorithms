

# 재귀함수 방식 : 재귀함수는 계속되는 함수의 호출에 따라 오버헤드가 발생할 수 있으므로 반복문을 사용하는 것이 좋음.
# 탑다운 방식 : 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식
# d = [0] * 100
# for i in range(1,3) :
#     d[i] = 1

# def fibo(n) :
#     if d[n] != 0 :
#         return d[n]
#     d[n] = fibo(n-1) + fibo(n-2)
#     return d[n]

# print(fibo(6))

# 반복적 방식
# 보텀업 방식 : 작은 문제부터 차근차근 답을 도출한다. 
d = [0] * 100
d[1] = 1
d[2] = 1
n = 98

for i in range(3,n+1) :
    d[i] = d[i-1] + d[i-2]

print(d[n]) 