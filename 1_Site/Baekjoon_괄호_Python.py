
N = int(input())

result = []
for _ in range(N) :
    temp = list(input())
    stack = []
    flag = False
    for t in temp : 
        if t == '(' :
            stack.append(1)
        else :
            if stack :
               stack.pop()
            else :
                result.append('NO')
                flag = True
                break
    if flag == False :
        if stack :
            result.append('NO')
        else :
            result.append('YES')

for r in result :
    print(r)