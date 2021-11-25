
n = int(input())

graph = []

for i in range(n) :
    graph.append(list(map(int, input())))

def search (n,x,y) :
    if n == 1 :
        return graph[y-1][x-1]
    else :
        temp = "(" + str(search(n//2,x-(n//2),y-(n//2))) + str(search(n//2,x,y-(n//2))) + str(search(n//2,x-(n//2),y)) + str(search(n//2,x,y)) + ")"
        
    if temp == "(0000)" :
        return 0
    elif temp == "(1111)" :
        return 1
    else :
        return temp
        
print(search(n,n,n))