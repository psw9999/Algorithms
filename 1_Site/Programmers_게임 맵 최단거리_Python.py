def dfs(maps,x,y,f_x,f_y,expense) :
    
    if x == f_x and y == f_y :
        return expense
    
    if x >= 0 and y >= 0 and x <= f_x and y <= f_y and (maps[y][x] == 1 or maps[y][x] > expense):
        maps[y][x] = expense + 1
        result = min([
            dfs(maps,x-1,y,f_x,f_y,expense+1),
            dfs(maps,x+1,y,f_x,f_y,expense+1),
            dfs(maps,x,y+1,f_x,f_y,expense+1),
            dfs(maps,x,y-1,f_x,f_y,expense+1),
        ])
        return result
        
    else :
        return 100000
    
def solution(maps):
    f_x,f_y = len(maps[0])-1,len(maps)-1
    for 
    result = dfs(maps,0,0,f_x,f_y,1)
    if(result == 100000) :
        return -1
    
    return result
        
       
