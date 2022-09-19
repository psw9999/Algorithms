
import sys

input = sys.stdin.readline

N = int(input().rstrip())
strings = []

for _ in range(N) :
    temp = input().rstrip()
    strings.append(temp)

strings.sort(key=lambda x: len(x), reverse=True)
stringSet = set()
result = 0
for s in strings :
    if s not in stringSet :
        result += 1
        for i in range(len(s)) :
            stringSet.add(s[:i+1])

print(result)