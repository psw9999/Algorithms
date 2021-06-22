""" 문제1
import time

start_time = time.time()
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

temp = (first*k) + second
result = temp * (m//(k+1))
result += k*(m%(k+1))

end_time = time.time()
print("time :",end_time-start_time)
print(result)
"""

n,m = map(int,input().split())
max = 0
for j in range(n) :
    min = 10000
    temp_list = []
    for i in range(m) :
        temp_list.append(input().split())
    temp_list = map(int,temp_list)
    print(temp_list)
    if(max < min) :
        max = min
print(max)