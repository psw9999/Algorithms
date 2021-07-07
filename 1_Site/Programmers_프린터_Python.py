from collections import deque

def solution(priorities, location):
    set_priorities = list((set(priorities)))
    set_priorities.sort(reverse=True)
    target = priorities[location]
    priority_queue = deque(priorities)
    priority_queue[location] = 0
    result = 0
    
    for n in set_priorities :
        if n == target :
            break
        cnt = priority_queue.count(n)
        print(priority_queue)
        for i in range(len(priority_queue)) :
            temp = priority_queue.popleft()
            if n != temp :
                priority_queue.append(temp)
            else :
                result += 1
                cnt-=1
                if(cnt == 0) :
                    break
                
    for i in priority_queue :
        if i == target :
            result += 1
        elif i == 0 :
            return result+1
        
    return result+1