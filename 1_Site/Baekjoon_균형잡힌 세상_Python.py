array = []

while(1) :
    temp = list(input())
    if temp[0] == '.' :
        break
    array.append(temp)
    
for arr in array :
    stack = []
    flag = False
    for i in arr :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ')' :
            if len(stack) == 0 or stack[-1] != '(' :
                print('no')
                flag = True
                break
            else :
                stack.pop()
        elif i == ']' :
            if  len(stack) == 0 or stack[-1] != '[' :
                print('no')
                flag = True
                break
            else :
                stack.pop()
    if flag == False :
        if len(stack) == 0 :
            print('yes')
        else :
            print('no')
    
