
from inspect import trace
import sys
input = sys.stdin.readline    

N,r,c = map(int, input().rstrip().split())

start = 0
tr,tc = 0,0
# 최대 나올 수 있는 값
value = (4**N)-1

while N > 0 :
    quad = []
    quad.append([(tr,tr+2**(N-1)-1),(tc,tc+2**(N-1)-1)])
    quad.append([(tr,tr+2**(N-1)-1),(tc+2**(N-1),tc+(2**N)-1)])
    quad.append([(tr+2**(N-1),tr+(2**N)-1),(tc,tc+2**(N-1)-1)])
    quad.append([(tr+2**(N-1),tr+(2**N)-1),(tc+2**(N-1),tc+(2**N)-1)])
    # print(quad)
    
    for i in range(len(quad)) :
        if quad[i][0][0] <= r <= quad[i][0][1] :
            if quad[i][1][0] <= c <= quad[i][1][1] :
                value = value - ((4**(N-1)) * (3-i))
                tr,tc = quad[i][0][0], quad[i][1][0]
                # print(value)
                # print(i)
    N-=1 

print(value)