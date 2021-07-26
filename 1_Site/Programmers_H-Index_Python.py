# 문제풀이
# 1. 문제를 이상하게 해석하여서 (h가 반드시 배열 내의 값으로 되어야 하는것으로 해석했다.) 시간이 좀 걸렸다.
# 2. 조건이 'h번 이상이 h편 이상'이므로 h는 배열의 길이 값을 넘을 수 없어 첫번째 인덱스부터 배열의 길이 값을 넘는지 체크하였다.
# 3. 만약 배열의 끝까지 해당 조건을 만족하지 못하면 ([0,0,0,...])] 0을 반환하도록 하였다.
# 4. 다른 사람과 풀이를 비교하였는데 대부분의 풀이가 매우 흡사하였다.

def solution(citations):
    citations.sort()
    lens = len(citations)
    for i in range(len(citations)) :
        if citations[i] >= lens-i :
            return lens-i
    
    return 0