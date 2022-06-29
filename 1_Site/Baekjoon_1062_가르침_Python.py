import sys
import re
from itertools import combinations

input = sys.stdin.readline
if __name__ == "__main__":
    
    def word2bit(word):
        res = 0
        for w in word :
            res|=1<<w
        return res
    
    N,K = map(int, input().split())
    basic = set()
    for a in ['a','c','i','n','t'] :
        basic.add(ord(a)-ord('a'))
    learned = 0
    for i in basic:
        learned |= (1<<i)

    words = []
    candidates = set()
    for _ in range(N) :
        temp = re.sub('a|n|t|c|i','', input().rstrip())
        s = set()
        for t in temp :
            v = ord(t) - ord('a')
            s.add(v)
            candidates.add(v)
        words.append(s)

    wordbits = [word2bit(word) for word in words]
    result = 0
    if K<5:
        print(0)
        exit()
    elif len(candidates) <= (K-5):
        print(N)
        exit()
    else:
        bitMask = (1<<26) - 1
        for c in combinations(candidates,K-5):
            cnt = 0
            tmp = learned
            for i in c:
                tmp |= (1<<i)
            tmp ^= bitMask
            
            for wordbit in wordbits :
                if (wordbit & tmp) == 0 :
                    cnt += 1
            
            result = max(cnt, result)
        print(result)