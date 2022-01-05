
from collections import deque

N,K = map(int,input().split())

if K <= N :
    print(N - K)
    while N >= K :
        print(N, end=' ')
        N-=1
    exit(0)

visited = [0] * 100001
visited[N] = 1

queue = deque()
queue.append((N,[N]))

def check_answer(v,visited_list) :
    global K, queue
    if v == K :
        print(len(visited_list)-1)
        for vl in visited_list :
            print(vl, end = ' ')
        exit(0)
    
    if v >= 0 and v < 100001 :
       # if visited[v] == 0 or visited[v] > len(visited_list) : 
       if visited[v] == 0 :
            queue.append((v, visited_list))
            visited[v] = len(visited_list)

while queue :
    temp, temp_visited = queue.popleft()
    
    check_answer(temp*2,temp_visited+[temp*2])
    check_answer(temp-1,temp_visited+[temp-1])
    check_answer(temp+1,temp_visited+[temp+1])

# 다른 사람 코드
# 이전 값을 다른 배열에 저장하여 찾아가는 방식으로 queue에 리스트를 추가하는 방식보다 훨씬 빠름.
# from collections import deque
# N,K=map(int,input().split(' '))
# dist=[0]*100001
# move=[0]*100001
# answer=[]
# def bfs(start):
#     global answer1,answer2
#     visited=[]
#     queue=deque([])
#     queue.append(start)
#     while(queue):
#         outX=queue.popleft()
#         if outX==K:
#             answer.append(K)
#             tmp=move[K]
#             for _ in range(dist[K]):
#                 answer.append(tmp)
#                 tmp=move[tmp]             
#             return
#         for i in (outX+1,outX-1,outX*2):
#             if 0<=i<100001 and dist[i]==0:
#                 queue.append(i)
#                 dist[i]=dist[outX]+1
#                 move[i]=outX
# bfs(N)
# print(dist[K])
# print(' '.join(map(str, answer[::-1])))
