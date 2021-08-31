
# 나의 풀이 및 수정할 점

def solution(table, languages, preference):
    max_score = 0
    result = ''
    for i in range(len(table)) : 
        # .split()은 리스트형으로 반환하므로 굳이 list 타입으로 변환할 필요가 없음.
        #temp = list(table[i].split(' '))
        temp = table[i].split(' ')
        temp_score = 0
        
        # 반복문을 1부터 시작하면 굳이 0을 비교하는 if문이 필요 없어짐.
        #for j in range(len(temp)) :
        for j in range(1, len(temp)) :
            #if j != 0 :
                # for e in range(len(languages)) :
                #     if languages[e] == temp[j] : 
                #         temp_score += preference[e] * (6-j)
            for e in range(len(languages)) :
                if languages[e] == temp[j] : 
                    temp_score += preference[e] * (6-j)
        
        if temp_score > max_score :
            max_score = temp_score
            result = temp[0]
        # and 연산자로 if문을 하나로 줄일 수 있음.
        #elif temp_score == max_score :
            #if result > temp[0] : 
        elif temp_score == max_score and result > temp[0] :
                result = temp[0]
                
    return result

# 다른 사람의 풀이
# def solution(table, languages, preference):
#     answer = 'ZZZZZZZZ'
#     score_dic = {lang: score for lang, score in zip(languages, preference)}
#     max_score = 0
#     for row in table:
#         r = row.split(' ')
#         curr_score = 0
#         for i in range(1, len(r)):
#             curr_score += score_dic.get(r[i], 0) * (6-i)
#         if max_score < curr_score:
#             max_score = curr_score
#             answer = r[0]
#         elif max_score == curr_score and answer > r[0]:
#             answer = r[0]

#     return answer