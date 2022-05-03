import re
from collections import defaultdict

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower() 
    temp1, temp2 = defaultdict(int), defaultdict(int)
    pattern = re.compile('[^a-z]')
    
    for i in range(len(str1)-1) :
        temp = re.sub(pattern, "", str1[i:i+2])
        if len(temp) != 2 :
            continue
        temp1[temp] += 1
        
        
    for i in range(len(str2)-1) :
        temp = re.sub(pattern,"",str2[i:i+2])
        if len(temp) != 2 :
            continue
        temp2[temp] += 1
    
    share, sumV = 0,0
    share, sumV = calcul(temp2, temp1)
    
    if share == 0 and sumV == 0 :
        share,sumV = 1,1
    print(share, sumV)
    return int((share / sumV) * 65536)

def calcul(temp1, temp2) :
    share, sumV = 0,0
    temp = set()
    temp.update(temp1.keys())
    temp.update(temp2.keys())
    for k in temp :
        share += min(temp1[k],temp2[k])
        sumV += max(temp1[k],temp2[k])
    
    return share, sumV
    
    
    
    
        