import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
words = defaultdict(int)
fullWords = defaultdict(int)
queue = []
result = 0

for _ in range(N) :
    word = input().rstrip()
    
    # 중복 제거
    if fullWords[word] >= 1 :
        continue
    
    fullWords[word] += 1
    queue.append(word)
    
    for i in range(1, len(word)+1) :
        temp = word[:i]
        words[temp] += 1
        if words[temp] >= 2 and (len(temp) > result) :
            result = len(temp)

# 정답 출력
if result > 0 :
    r = ""
    
    for word in queue :
        if len(word) < result :
            continue
        temp = word[:result]
        
        if r == "" :
            if words[temp] >= 2 :
                r = temp
                print(word) 
        
        elif r in word[:result] :
            print(word)
            break

