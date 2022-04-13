def timeConvert(time, minute, second) :
    return (time*60*60) + (minute * 60) + second

def solution(play_time, adv_time, logs):
    h, m, s = map(int, play_time.split(":"))
    DP = [0] * (timeConvert(h,m,s)+1)
    
    h, m, s = map(int, adv_time.split(":"))
    adv = timeConvert(h,m,s)-1
    
    for log in logs :
        start, end = map(str, log.split("-"))
        sh,sm,ss = map(int, start.split(":"))
        eh,em,es = map(int, end.split(":"))
        DP[timeConvert(sh,sm,ss)] += 1
        DP[timeConvert(eh,em,es)] -= 1
    
    maxV = DP[0]
    timeCnt = DP[0]
    result = "00:00:00"
    
    for i in range(1, len(DP)) :
        DP[i] = DP[i-1] + DP[i]
        timeCnt += DP[i]
        
        if i >= adv :
            if timeCnt > maxV :
                temp = i - adv
                th = temp // 3600
                tm = (temp % 3600) // 60
                ts = (temp % 60)
                result = "%02d:%02d:%02d"%(th,tm,ts)
                maxV = timeCnt
            timeCnt -= DP[i-adv]
    return result
        
        