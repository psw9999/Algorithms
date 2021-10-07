# 1. 내 풀이는 enter를 기준으로, 다른 사람 풀이는 leave를 기준으로 반복문을 작성하였다.
# 2. 나도 처음에 그 방법을 생각하였으나, 만나는 사람의 수를 세는데 어려움을 겪어서 지금 방법을 선택했다.
# 3. 다른 사람의 풀이가 더 깔끔하다..


# 내 풀이
def solution(enter, leave):
    result = [0 for i in range(len(enter))]
    temp = []
    j = 0

    for i in enter :
        temp.append(i)
        result[i-1] += len(temp)-1
        for x in range(len(temp)-1) :
            result[temp[x]-1] += 1

        while leave[j] in temp :
            temp.remove(leave[j])
            if j < len(leave)-1 :
                j+=1

    return result

# 다른 사람의 풀이 1
def solution(enter, leave):
    answer = [0] * len(enter)

    room = []
    e_idx = 0
    for l in leave:
        while l not in room:
            room.append(enter[e_idx])
            e_idx += 1
        room.remove(l)
        for p in room:
            answer[p - 1] += 1
        answer[l - 1] += len(room)

    return answer