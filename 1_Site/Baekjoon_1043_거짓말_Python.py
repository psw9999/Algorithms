
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N,M = map(int, input().rstrip().split())
party_visited = [False] * (M)
person_visited = [False] * (N+1)
queue = deque()
temp = list(map(int, input().rstrip().split()))
for person in temp[1:] :
    person_visited[person] = True
    queue.append(person)

person_dict = defaultdict(list)
party_list = []
for i in range(M) :
    temp = list(map(int, input().rstrip().split()))
    party_list.append(temp[1:])
    for person in temp[1:] :
        person_dict[person].append(i)

while queue :
    person = queue.popleft()
    for party in person_dict[person] :
        if party_visited[party] == False :
            party_visited[party] = True
            for p in party_list[party] :
                if person_visited[p] == False :
                    person_visited[p] = True
                    queue.append(p)

print(party_visited.count(False))




