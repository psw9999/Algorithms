def solution(n, k, cmd):
    table = []
    cur = k
    for i in range(n) :
        front = i - 1
        rear = i + 1
        table.append([True,i-1,i+1])
    
    delete = []
    for command in cmd :
        temp = command.split()
        if temp[0] == "D" :
            for i in range(int(temp[1])) :
                cur = table[cur][2]
        
        elif temp[0] == "U" :
            for i in range(int(temp[1])) :
                cur = table[cur][1]
        
        elif temp[0] == "C" :
            front,rear = table[cur][1], table[cur][2]                
            table[cur][0] = False
            table[front][2] = rear
            delete.append(cur)
            if rear < n :
                table[rear][1] = front
                cur = rear
            else :
                cur = front
                
        elif temp[0] == "Z" :
            recent = delete.pop()
            table[recent][0] = True
            front, rear = table[recent][1],table[recent][2]
            table[front][2] = recent
            if rear < n :
                table[rear][1] = recent
        
    
    result = ""
    for status, front, rear in table :
        if status == True :
            result = result + "O"
        else :
            result = result + "X"
    
    return result