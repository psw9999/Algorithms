
K = int(input())

sign = list(map(str, input().split()))

number = {}

minMax= [0,9876543210]

for i in range(10) :
    number[i] = 0

def back(cnt, result, number) :
    global minMax
    if cnt == K :
        minMax[0] = max(result, minMax[0])
        minMax[1] = min(result, minMax[1])
        return
    
    for j in range(10) : 
        if number[j] == 0 :
            if sign[cnt] == '>' :
                if (result%10) > j :
                    number[j] = 1
                    back(cnt+1,result*10 + j,number)
                    number[j] = 0
            else :
                if (result%10) < j :
                    number[j] = 1
                    # 0이 맨 앞자리라면?
                    back(cnt+1,result*10 + j,number)
                    number[j] = 0


for i in range(10) :
    number[i] = 1
    back(0,i,number)
    number[i] = 0

for m in minMax :
    m = str(m)
    if len(m) < K+1 :
        print('0' + m)
    else :
        print(m)
        
# 다른 사람 풀이
# 0~9까지 순차적으로 계산하기 때문에 맨 처음 통과된 값이 최소값이므로 일일이 최솟값 계산이 필요없다
# 또, 마지막으로 대입된 값이 최댓값이므로 값이 완성되면 항상 갱신하도록 하였다.
# 미리 값을 문자열화(str) 시켜놓고 비교할 인덱스값도 문자열화 하여 비교시키는 것이 편리해보인다.

# def possible(item1, item2, symbol):
#     if symbol == '<':
#         return item1 < item2
#     if symbol == '>':
#         return item1 > item2

# def backtracking(idx, string):
#     global min_value
#     global visited
#     global max_value
#     if idx == n + 1:
#         if not len(min_value):
#             min_value = string
#         else:
#             max_value = string
#         return
#     for i in range(10):
#         if visited[i]:
#             continue
#         if idx == 0 or possible(string[-1], str(i), stack[idx - 1]):
#             visited[i] = True
#             backtracking(idx + 1, string + str(i))
#             visited[i] = False


# if __name__ == '__main__':
#     n = int(input())
#     stack = list(input().split())
#     max_value = ''
#     min_value = ''
#     visited = [False] * 10
#     backtracking(0, '')
#     print(max_value)
#     print(min_value)