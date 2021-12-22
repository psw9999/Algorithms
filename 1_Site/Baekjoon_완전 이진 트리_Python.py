
K = int(input())

graph = list(map(int,input().split()))

arr = [(0, len(graph))]
idx = 0
for i in range(K) :
    for j in range(2 ** i) :
        start, end = arr[idx]
        idx += 1
        mid = (start + end) // 2
        print(graph[mid], end = ' ')
        arr.append((start, mid-1))
        arr.append((mid+1,end))
    print()