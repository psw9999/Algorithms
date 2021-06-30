from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    total = 0
    vacant = False
    n = 0
    bridge_queue = deque()
    truck_queue = deque(truck_weights)
    
    while True :
        if len(truck_queue) > 0 and weight >= total+truck_queue[0] and len(bridge_queue) <= bridge_length :
            temp = truck_queue[0]
            total += temp
            bridge_queue.append(temp)
            truck_queue.popleft()
            time += 1
            
        else :
            time += (bridge_length)
            total = 0
            n += (bridge_length)
            bridge_queue.popleft()            
            
        # else :     
        #     if vacant == True :
        #         time += 1
        #         total-=bridge_queue.popleft()
        #         n += 1
        #         if(len(bridge_queue) == 0) :
        #             vacant = False
        
            # elif vacant == False :
            #     vacant = True
            #     time += (bridge_length)

        print(bridge_queue,time)
        
        if n == len(truck_weights) :
            break
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    total = 0
    vacant = False
    n = 0
    bridge_queue = deque()
    truck_queue = deque(truck_weights)
    
    while True :
        if len(truck_queue) > 0 and weight >= total+truck_queue[0] and len(bridge_queue) <= bridge_length :
            temp = truck_queue[0]
            total += temp
            bridge_queue.append(temp)
            truck_queue.popleft()
            time += 1
            
        else :
            time += (bridge_length)
            total = 0
            n += (bridge_length)
            bridge_queue.popleft()            
            
        # else :     
        #     if vacant == True :
        #         time += 1
        #         total-=bridge_queue.popleft()
        #         n += 1
        #         if(len(bridge_queue) == 0) :
        #             vacant = False
        
            # elif vacant == False :
            #     vacant = True
            #     time += (bridge_length)

        print(bridge_queue,time)
        
        if n == len(truck_weights) :
            break
    return time

bridge_length = 2
weight = 10
truck_weight = [7,4,5,6]

print(solution(bridge_length, weight, truck_weight))