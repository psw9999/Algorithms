def scoreCalcul(info, cur) :
    myScore, oppScore,digit = 0,0,0
    for i in range(11) :
        if info[i] == 0 and cur[i] == 0 :
            continue
        digit += cur[i] * (i+1)
        if info[i] >= cur[i] :    
            oppScore += 10 - i
        else :
            myScore += 10 - i
    return myScore - oppScore, digit

def dfs(info, arrows, cur, i) :
    global result, highScore,digit

    # 화살을 모두 쏜 경우
    if arrows == 0:
        score,tDigit = scoreCalcul(info, cur)
        if score > 0 and score > highScore :
            result = cur[:]
            highScore = score
            digit = tDigit
        elif score > 0 and score == highScore :
            if tDigit > digit :
                digit = tDigit
                result = cur[:]
        return

    # 0점까지 온 경우
    if i == 10 :
        cur[10] = arrows
        score,tDigit = scoreCalcul(info, cur)
        if score > 0 and score > highScore :
            result = cur[:]
            highScore = score
            digit = tDigit
        elif score > 0 and score == highScore :
            if tDigit > digit :
                digit = tDigit
                result = cur[:]
        return

    # 이기는 경우
    if arrows > info[i] :
        cur[i] = info[i] + 1
        dfs(info, arrows-(info[i]+1), cur[:], i+1)
        cur[i] = 0
    # 지는 경우
    dfs(info, arrows, cur[:], i+1)


def solution(n, info):
    global result, highScore, digit
    result = [-1]
    highScore = 0
    digit = 0
    cur = [0,0,0,0,0,0,0,0,0,0,0]
    dfs(info, n, cur[:], 0)

    return result