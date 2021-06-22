def solution(s):
    
    #word_list = s.split()      #문제의 조건이 하나 이상의 공백문자임, 공백문자가 여러개여도 s.split()을 실행시 문자만 가져와 리스트에 저장함.
    word_list = s.split(" ")    #반면, split(" ")으로 실행시 공백문자가 여러개면, 하나의 공백문자만 제외하고 나머지 공백문자는 리스트에 저장함.
    for i in range(len(word_list)):
        spell_list = list(word_list[i])
        
        for j in range(len(spell_list)):
            if(j%2==0) :
                spell_list[j] = spell_list[j].upper()
            else :
                spell_list[j] = spell_list[j].lower()
                
        word_list[i] = "".join(spell_list)

    answer = " ".join(word_list)
    return answer
