import sys

def calculate(num1, symbol, num2) :
    num1 = int(num1)
    num2 = int(num2)
    if symbol == '+' :
        return num1 + num2
    elif symbol == '-' :
        return num1 - num2
    elif symbol == '*' :
        return num1 * num2
    
def dfs(idx, value) :
    global N,math,max_value
    print(value)
    if idx > (N-1) :
        max_value = max(max_value,value)
        return
    
    if idx == 0 :
        oper = '+'
    else :
        oper = math[idx-1]
        
    if (idx+2) < N : 
        temp = calculate(math[idx],math[idx+1],math[idx+2])
        dfs(idx+4, calculate(value,oper,temp))
    
    dfs(idx+2, calculate(value,oper,math[idx]))
        
    
input = sys.stdin.readline
N = int(input())

math = list(input().rstrip())
max_value = -2e31
dfs(0,0)
print(max_value)

