
# 리뷰
# 1. 슬라이싱 기능에 대하여 망각하고 있었던 것 같다. 리스트의 범위를 지정하여 사용하는 방법은 슬라이싱을 통해 코드를 상당히 줄일 수 있으므로 참조해야겠다.

# 내가 작성한 코드
# def solution(array, commands):
#     result = []
#     for i in range(len(commands)) :
#         i, n, m = commands[i][0]-1,commands[i][1]-1, commands[i][2]-1
#         temp = []
#         while i <= n :
#             temp.append(array[i])
#             i+=1
#         temp.sort()
#         result.append(temp[m])       
#     return result

# 다른사람의 코드
def solution(array, commands) :
    result = []
    for command in commands :
        i,j,k = command[0], command[1], command[2]
        # 슬라이싱시 마지막 번호는 1을 빼지 않아도 된다.
        result.append(sorted(commands[i-1:j])[k-1])
    return result
