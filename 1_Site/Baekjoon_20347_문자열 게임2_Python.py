
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input().rstrip())
result = []
for t in range(T) :
    result.append([])
    str_arr = input().rstrip()
    K = int(input().rstrip())
    
    # if K == 1 :
    #     result[t].append(1)
    #     result[t].append(len(str_arr))
    #     continue
    
    wordDict = defaultdict(list)
    for idx,str in enumerate(str_arr) :
        wordDict[str].append(idx)
    
    #print(wordDict)
    listCnt = 0
    for wordlist in wordDict.values() :
        listCnt = max(listCnt, len(wordlist))
    if listCnt < K :
        result[t].append(-1)
        continue
        
    minV = 10000
    maxV = 0
        
    for wordlist in wordDict.values() :
        if len(wordlist) >= K :
            for i in range(len(wordlist)-K+1) :
                temp = wordlist[i+K-1] - wordlist[i] + 1
                minV = min(minV,temp)
                maxV = max(maxV,temp)
    
    result[t].append(minV)
    result[t].append(maxV)

for r in result :
    print(*r)
    
    
    