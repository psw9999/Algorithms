def solution(s):
    result = len(s)
    length = len(s)
    
    # n : 문자열 자르는 단위
    for n in range(1,(length//2)+1) :
        bef = s[0:n]
        cnt = 1
        cur_len = length
        # i : 문자열 끝까지 진행하도록
        for i in range(n,len(s),n) :
            if i+n > length :
                break
            cur = s[i:i+n]

            if bef == cur :
                cur_len -= n
                cnt += 1
            else :
                bef = cur
                if cnt == 1:
                    continue
                else :
                    cur_len += len("{}".format(cnt))
                    cnt = 1
            
        if cnt > 1 :
            cur_len += len("{}".format(cnt))
            cnt = 1
        result = min(result, cur_len)
    
    return result