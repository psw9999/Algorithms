# 개선점
# 1. stack_cnt를 통해 배열의 마지막 위치를 찾아갔는데, 슬라이싱을 통해 마지막 배열부터 비교하기

def solution(board, moves):
    stack = []
#    stack_cnt = 0
    result = 0
    for i in moves :
        i-=1
        for line in board :
            if line[i] != 0 :
                stack.append(line[i])
#                stack_cnt+=1
                if len(stack) > 1 :
#                    if stack[stack_cnt-2] == stack[stack_cnt-1] :
                     if stack[-2] == stack[-1] :
                        stack.pop()
                        stack.pop()
#                        stack_cnt-=2
                        result+=2
                line[i] = 0
                break

    return result