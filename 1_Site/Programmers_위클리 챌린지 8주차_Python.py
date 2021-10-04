# 1. max 함수를 잘 활용하자.
# 2. 스왑 방식을 잘 생각하자.
# 3. 이차원 배열은 다음과 같은 for문 방식을 사용할 수 있다.


# 내 소스
def solution(sizes):
    f_max = 0
    s_max = 0
    for i in sizes :
        if i[0] >= i[1] :
            if i[0] > f_max :
                f_max = i[0]
            if i[1] > s_max : 
                s_max = i[1]
        else :
            if i[1] > f_max :
                f_max = i[1]
            if i[0] > s_max :
                s_max = i[0]
    
    return (f_max * s_max)

# 다른사람 소스
# def solution(sizes):
#     row = 0
#     col = 0
#     for a, b in sizes:
#         if a < b:
#             a, b = b, a
#         row = max(row, a)
#         col = max(col, b)
#     return row * col