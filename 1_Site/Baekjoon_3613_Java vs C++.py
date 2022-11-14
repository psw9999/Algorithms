import sys
from collections import deque

input = sys.stdin.readline

word = deque(list(input().rstrip()))

language = ""
result = ""

if word[0].isupper() or word[0] == "_" :
    print("Error!")
    exit(0)

while word :
    w = word.popleft()
    if w.islower() :
        result += w
    
    elif w == "_" and language != "Java" and len(word) > 0 and word[0].islower() :
        language = "C"
        result += word.popleft().upper()
    
    elif w.isupper() and language != "C" :
        language = "Java"
        result = result + "_" + w.lower()
    
    else :
        print("Error!")
        exit(0)

print(result)
