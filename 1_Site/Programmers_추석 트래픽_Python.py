SECOND = 1000
MINUTE = SECOND * 60
HOUR = MINUTE * 60

INIT_TIME = 2999

def timeSplit(times, dispose):
    times = list(map(int, times.replace(".",":").split(":")))
    endTime = INIT_TIME + (times[3] + (times[2] * SECOND) + (times[1] * MINUTE) + (times[0] * HOUR))
    startTime = endTime - float(dispose.replace("s",""))*1000 + 1
    return startTime, endTime

def checkTime(tasks, start, end):
    result = 0
    for task in tasks :
        if task[0] <= end and task[1] >= start :
            result += 1
    return result
    

def solution(lines):
    tasks = []
    # 처리시간 담기
    for idx,line in enumerate(lines) :
        times = line.split(" ")
        startTime, endTime = timeSplit(times[1], times[2])
        tasks.append((startTime, endTime))
        
    result = 0
    # 1초간 몇개의 처리시간 있는지 확인 (시작시간)
    for task in tasks:
        result = max(result, checkTime(tasks, task[0], task[0]+999), checkTime(tasks, task[1], task[1] + 999))
        
    return result
        
            
        
        