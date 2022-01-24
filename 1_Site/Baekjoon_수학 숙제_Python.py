
import sys
import re

input = sys.stdin.readline

N = int(input())
paper = [] 
result = str()
for i in range(N):
    temp = input().rstrip()
    for j in list(re.split("\D", temp)):
        if j != "": 
            paper.append(int(j))
paper.sort()
for i in paper: 
    result+=str(i)+"\n"
    
print(result.rstrip())