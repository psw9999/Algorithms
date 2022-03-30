import heapq
def solution(operations):
    queue = []
    for operation in operations :
        d, value = operation.split()
        value = int(value)
        
        if d == 'I' :
            heapq.heappush(queue,value)
        
        else :
            if not queue :
                continue
            
            if value == 1 :
                queue = heapq.nlargest(len(queue),queue)[1:]
                heapq.heapify(queue)
            
            elif value == -1 :
                heapq.heappop(queue)
    
    if queue :
        return [heapq.nlargest(1,queue)[0],heapq.heappop(queue)]
    else :
        return [0,0]