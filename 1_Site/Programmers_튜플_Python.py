from copy import deepcopy
def solution(s):
    string_list = s[2:-1].replace('},','').replace('}','').split('{')
    result = []
    string_list.sort(key = lambda x : len(x))
    compare_dict = {}
    
    for i, string in enumerate(string_list) :
        temp_list = list(map(int, string.split(',')))
        temp_dict = deepcopy(compare_dict)
        for temp in temp_list :
            if temp not in temp_dict :
                result.append(temp)
                compare_dict[temp] = 1
                break
            elif temp_dict[temp] == 0 :
                result.append(temp)
                compare_dict[temp] += 1
                break
            else :
                temp_dict[temp] -= 1
    
    return result
                
            
        
    