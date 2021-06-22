
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


