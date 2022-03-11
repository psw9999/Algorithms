from collections import defaultdict
        
def solution(gems):
    typeCnt = len(set(gems))
    aLeft,aRight = 0, len(gems)-1
    left,right = 0,0
    gemDict = defaultdict(int)
    
    while right < len(gems) :
        gemDict[gems[right]] += 1
        
        if len(gemDict) == typeCnt :
            while left <= right :
                if gemDict[gems[left]] >= 2:
                    gemDict[gems[left]] -= 1
                    left += 1
                else :
                    if (aRight - aLeft) > (right - left) :
                        aRight, aLeft = right, left
                    break      
        right += 1
        
    return [aLeft + 1, aRight + 1]