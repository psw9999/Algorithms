from heapq import heappush, heappop, heapify

def solution(scoville, K):
    result = 0
    heapify(scoville)
    
    while len(scoville) > 1 :
        heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
        result += 1
        if scoville[0] >= K:
            return result
    
    return -1