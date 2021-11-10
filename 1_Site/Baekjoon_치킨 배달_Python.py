from itertools import combinations

n,m = list(map(int, input().split()))

array = [[0]*n for i in range(n)]
home_arr = []
chicken_arr = []

result = []

for i in range(n) :
    array[i] = list(map(int, input().split()))

for i in range(len(array)) :
    for j in range(len(array[i])) :
        if array[i][j] == 1 :
            home_arr.append((i,j))
        elif array[i][j] == 2 :
            chicken_arr.append((i,j))

for chickenArea in list(combinations(chicken_arr,m)) :
    home_dist = 0
    for hy, hx in home_arr :
        dists = []
        for cy, cx in chickenArea :
            dist = abs(hy-cy) + abs(hx-cx)
            dists.append(dist)
            
        home_dist += min(dists)
    result.append(home_dist)    
print(min(result))
             
    