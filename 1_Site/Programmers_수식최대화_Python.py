import re
from collections import deque
from copy import deepcopy
def dfs(numbers,signs,visited,key) :
    global result
    
    values = visited.values()
    visited[key] = True
    
    for i in range(len(numbers)-1) :
        first = numbers.popleft()
        sign = signs.popleft()
        second = numbers[0]
        
        temp = 0
        if sign == key :
            if key == '-' :
                temp = first - second
            elif key == '*' :
                temp = first * second
            else :
                temp = first + second
            numbers[0] = temp
        
        else :
            numbers.append(first)
            signs.append(sign)
    
    numbers.append(numbers.popleft())
    
    if False not in values :
        result = max(result, abs(numbers[0]))
        #print(numbers)
        return 
        
    for key in visited.keys() :
        if visited[key] == True :
            continue
        dfs(deepcopy(numbers),deepcopy(signs),visited,key)
        visited[key] = False
        
    
def solution(expression):
    global result
    result = 0
    
    pattern = re.compile('[-*+]')
    numbers = deque(list(map(int,re.split(pattern, expression))))
    signs = deque(re.findall(pattern,expression))
    
    visited = {'*' : False, '-': False, '+' : False}
    
    for key in visited.keys() :
        dfs(deepcopy(numbers),deepcopy(signs),visited,key)
        visited[key] = False
    
    return result