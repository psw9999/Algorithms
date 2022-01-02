from collections import deque

S = list(input())
T = list(input())

queue = deque()
queue.append(T)

while queue :
    temp = queue.popleft()
    if temp == S :
        print(1)
        exit(0)
    if len(temp) <= len(S) :
        break
    if temp[0] == 'B' :
        queue.append(list(reversed(temp[1:])))
        print(list(reversed(temp[1:])))
    if temp[-1] == 'A' :
        queue.append(temp[:-1])
        print(temp[:-1])

print(0)
        

