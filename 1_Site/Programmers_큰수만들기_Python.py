# 코드 리뷰
# 1. 나는 문자열을 슬라이싱하여 앞자리와 비교하여 작은 수가 없어질 때까지 덮어쓰는 방식을 사용함.
# 2. 다른 사람의 코드는 스택을 사용하여 비교하는 수보다 작은 pop시키는 방법을 사용함.
# 3. 문자열 슬라이싱 방식보다는 스택을 사용하여 구현하는 것이 구현 난이도와 가독성 측면에서 더 좋은 것 같다.

def solution(number, k):
    result = number[0]
    cnt = k
    for i in range(1,len(number)) :
        for j in reversed(range(len(result))) :
            if(int(result[j]) < int(number[i])) :
                cnt-=1
                if cnt==0 : 
                    return result[:j] + number[i:]
            else :
                j+=1
                break

        result = result[:j] + number[i]
    return result[:-cnt]

# 다른 사람 코드
# def solution(number, k):
#     st = []
#     for i in range(len(number)):
#         while st and k > 0 and st[-1] < number[i]:
#             st.pop()
#             k -= 1
#         st.append(number[i])
#     return ''.join(st[:len(st) - k])