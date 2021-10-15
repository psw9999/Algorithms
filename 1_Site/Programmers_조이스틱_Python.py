def solution(name):
    result = 0
    A_Cnt = name.count('A')
    i = 0
    
    while True:

        if A_Cnt == len(name) : return result

        if name[i] != 'A' :
            A_cnt += 1
            name[i] = 'A'
            # 문자가 'Z'인 경우에는 한 칸 이동한 것이므로 +1을 함.
            result += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        
        left, right = 1,1
        # 현재 위치에서 왼쪽과 오른쪽 중 어디에 더 긴 'A'의 배열이 있는지 체크한다. 
            for l in range(1,len(name)):
            # 파이썬의 인덱스는 음수가 허용된다.
            if name[i-l] == 'A': left += 1
            else: break
        
        for r in range(1,len(name)):
            if name[i+r] == 'A': right += 1
            else: break
        
        if left < right:
            result += left
            i -= left
        else:
            result += right
            i += right
            
            
    return result