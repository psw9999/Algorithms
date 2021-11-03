# 공백문자가 여러개인 경우 (ex: 'abc   d')면 split()시 리스트 반환시 ['a','b','c','d']로 반환됨.
# 그런데 split(' ')사용시 공백문자가 여러개면 한개씩 구분하여 반환. (['a','b','c','d',' ',' ',' '])
def solution(s):
    s_list = s.split(' ')
    for i in range(len(s_list)) :
        s_list[i] = s_list[i].capitalize()
    
    return ' '.join(s_list)