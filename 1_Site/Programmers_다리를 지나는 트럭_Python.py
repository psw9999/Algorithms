from collections import deque

def solution(bridge_length, weight, truck_weights):
    total = 0
    time = 0
    bridge_queue = deque([0] * bridge_length)
    truck_queue = deque(truck_weights)

    while truck_queue :
        time += 1
        total-=bridge_queue.popleft()

        if(total+truck_queue[0] <= weight) :
            total += truck_queue[0]
            bridge_queue.append(truck_queue.popleft())

        else :
            bridge_queue.append(0)

    time += bridge_length

    return time
