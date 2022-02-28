
import sys
input = sys.stdin.readline

#str_arr = deque(list(input().rstrip()))
str_arr = input().rstrip()
#first = str_arr[0]
#print(str_arr)
# for _ in range(len(str_arr)) :
#     if first == str_arr[-1] :
#         str_arr.appendleft(str_arr.pop())
#     else :
#         break

a_cnt = str_arr.count('a')
temp = 0
for i in range(a_cnt) :
    if str_arr[i] == 'b' :
        temp += 1
result = temp


# for i in range(1, len(str_arr)-a_cnt+1) :
length = len(str_arr)
for i in range(1, length) :
    if str_arr[i-1] == 'b' : 
        temp -= 1
    if str_arr[(i+a_cnt-1)%length] == 'b' :
    #if str_arr[i+a_cnt-1] == 'b' :
        temp += 1 
    result = min(result, temp)

print(result)