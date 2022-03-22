import re
def solution(n, t, m, timetable):
    waiting = []
    pattern = re.compile('[:]')
    for time in timetable :
        hour,minute = map(int,re.split(pattern, time))
        waiting.append((hour*60) + minute)
    
    waiting.sort(reverse = True)
    cur_time = 9 * 60
    bus_queue = []
    
    for i in range(n) :
        cnt = 0
        bus_queue = []
        # 사람 태우기
        for j in range(len(waiting)-1,-1,-1) :
            if waiting[j] <= cur_time :
                bus_queue.append(waiting.pop())
                cnt+=1
            if cnt >= m :
                break
        
        if i < (n-1) :
            cur_time += t
    
    temp_time = 0
    if len(bus_queue) < m :
        temp_time = cur_time
    else :
        print(bus_queue)
        temp_time = bus_queue[-1]-1
    
    temp_hour = temp_time//60
    temp_minute = temp_time%60
    return "%02d:%02d"%(temp_hour, temp_minute)
