
from itertools import combinations
import sys

def search() :
    global graph
    
    for tx, ty in teacher :
        for i in range(tx,-1,-1) :
            if graph[ty][i] == 'S' :
                return False
            if graph[ty][i] == 'O' :
                break
        for i in range(ty,N) :
            if graph[i][tx] == 'S' :
                return False
            if graph[i][tx] == 'O' :
                break            
        for i in range(tx,N) :
            if graph[ty][i] == 'S' :
                return False
            if graph[ty][i] == 'O' :
                break
        for i in range(ty,-1,-1) :
            if graph[i][tx] == 'S' :
                return False
            if graph[i][tx] == 'O' :
                break
    return True
                             
input = sys.stdin.readline
N = int(input())

graph = [list(map(str, input().rstrip().split())) for _ in range(N)]

empty = []
teacher = []

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 'X' :
            empty.append((j,i))
        if graph[i][j] == 'T' :
            teacher.append((j,i))
            
for comb in combinations(empty,3) :
    for x,y in comb :
        graph[y][x] = 'O'
        
    if search() :
        print('YES')
        exit()
    
    for x,y in comb :
        graph[y][x] = 'X'

print('NO')    
