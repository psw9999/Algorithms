
import sys

input = sys.stdin.readline

N,M = map(int, input().rstrip().split())
keyword = {}
for _ in range(N) :
    keyword[input().rstrip()] = 1

result = []
total = N
for _ in range(M) :
    blog = list(input().rstrip().split(','))
    for b in blog :
        if b in keyword :
            if keyword[b] :
                total -= 1
                keyword[b] = 0
    #result.append(sum(keyword.values()))
    result.append(total)

for r in result :
    print(r)


