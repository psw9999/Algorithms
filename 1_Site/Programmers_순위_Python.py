import heapq
from collections import deque

heap = []
cur = 0

# 현재 시간 내에 있는 작업들 heap에 넣기
def task(jobs) :
    global heap, cur
    cnt = 0
    for i in range(len(jobs)) :
        s,c = jobs[0]
        if cur >= s :
            start,cost = jobs.popleft()
            heapq.heappush(heap,(c,s))
            if not jobs :
                return
        else :
            return
    
def solution(jobs):
    global heap, cur
    N = len(jobs)
    # 작업 요청 시간이 작은게 가장 오른쪽으로 가도록
    jobs.sort()
    jobs = deque(jobs)
    result = 0
    
    while jobs :
        if not heap :
            start, cost = jobs.popleft()
            cur = start + cost
            result += cost
            task(jobs)
                    
        while heap :
            cost,start = heapq.heappop(heap)
            cur += cost
            result += (cur - start)
            task(jobs)
    
    return (result // N)