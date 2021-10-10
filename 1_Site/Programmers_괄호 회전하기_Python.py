# 1. 문자를 하나씩 뒤로 미뤄서 붙이는 것은 굳이 deque를 안쓰고 해도 됐을 듯 (시간이 더 소요됨.)
# 2. 내 소스 코드의 문제 부분을 보면 같은 부분이 반복되고 있는데 딕셔너리를 사용하면 더 깔끔하게 해결 됐을 것 같다.

# 내 소스 코드
from collections import deque 

def solution(s):
    result = 0
    s = deque(s)
    
    for i in range(len(s)) :
        temp = []
        for j in range(len(s)) :
            if s[j] == '[' or s[j] == '(' or s[j] == '{' :
                temp.append(s[j])   
            else :
                if len(temp) == 0 :
                    temp.append('x')
                    break
                # 문제 부분
                elif temp[-1] == '{' :
                    if s[j] == '}' :
                        temp.pop()
                    else :
                        break
                elif temp[-1] == '(' :
                    if s[j] == ')' :
                        temp.pop()
                    else :
                        break
                elif temp[-1] == '[' :
                    if s[j] == ']':
                        temp.pop()
                    else :
                        break
        if len(temp) == 0 :
            result+=1
        s.append(s.popleft())
        
    return result

# 다른사람 소스
def check(x):
    stack = []
    dic = {'}': '{', ')': '(', ']': '['}

    for char in x:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if not stack:
                return False
            temp = stack.pop()
            if dic[char] != temp:
                return False
    if stack:
        return False
    return True

def rotate(lis, x):
    for i in range(x):
        lis = lis[1:] + lis[0]
    return lis

def solution(s):
    answer = 0
    for i in range(len(s)):
        temp = rotate(s, i)
        if check(temp):
            answer += 1
    return answer