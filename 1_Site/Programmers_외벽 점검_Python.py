from itertools import permutations

def solution(n, weak, dist):
    result = int(1e9)
    for i in range(len(weak)) :
        weak.append(weak[i]+n)
        
    for perm in permutations(dist, len(dist)) :
        # 시작 위치
        for start in range(len(weak)//2) :
            cur = start
            cnt = 0
            person = 0
            for p in perm :
                person += 1
                temp = weak[cur] + p
                for i in range(cur, len(weak)) :
                    if temp >= weak[i] :
                        cnt += 1
                        cur += 1
                    else :
                        break
                if cnt >= (len(weak)//2) :
                    result = min(result, person)
                    break
                #cur+=1
        
    if result == int(1e9) :
        result = -1
        
    return result