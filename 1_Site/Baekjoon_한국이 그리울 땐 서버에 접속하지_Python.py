
N = int(input())

pattern = input()
star = 0

for i in range(len(pattern)) :
    if pattern[i] == '*' :
        star = i
        
    
tail = len(pattern) - star
head = star
result = []
for _ in range(N) :
    temp = input()
    flag = True
    
    if len(temp) < len(pattern) - 1 :
        result.append("NE")
        continue
        
    for h in range(head) :
        if temp[h] != pattern[h] :
            result.append("NE")
            flag = False
            break
    
    if flag :
        for t in range(1,tail) :
            if temp[-t] != pattern[-t] :
                result.append("NE")
                flag = False
                break
            
        if flag : 
            result.append("DA")   

for r in result : 
    print(r)