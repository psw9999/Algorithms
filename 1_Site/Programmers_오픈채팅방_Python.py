from collections import deque,defaultdict
import re

def solution(record):
    queue = deque()
    uid_dict = defaultdict()
    
    for rec in record :
        temp = rec.split()
        
        if temp[0] != "Change" :
            queue.append((temp[0],temp[1]))
        if temp[0] != "Leave" :
            uid_dict[temp[1]] = temp[2]
    
    result = []
    while queue :
        act, uid = queue.popleft()
        temp = ""
        if act == "Enter" :
            temp = "%s님이 들어왔습니다."%(uid_dict[uid])
        elif act == "Leave" :
            temp = "%s님이 나갔습니다."%(uid_dict[uid])
        result.append(temp)
    
    return result