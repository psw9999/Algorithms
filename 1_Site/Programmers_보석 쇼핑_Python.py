from collections import defaultdict

def solution(gems):
    # 보석 종류 갯수 확인
    number = len(set(gems))
    current = 0
    result = [1,len(gems)]
    left, right = 0,0
    gemDict = defaultdict(int)
    
    # 인덱스 돌아다니면서 보석 갯수 확인
    for idx, gem in enumerate(gems) :
        gemDict[gem] += 1
        
        if gemDict[gem] == 1 :
            current += 1
            
        # 보석 갯수 최적화 하기
        while gemDict[gems[left]] >= 2 :
            gemDict[gems[left]] -= 1
            left += 1
        
        if current >= number :
            if (idx - left) < (result[1] - result[0]) :
                result = [left+1, idx+1]
    
    return result
