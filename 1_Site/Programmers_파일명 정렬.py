import re

def solution(files):
    temp = [re.split("([0-9]+)", file) for file in files]
    
    temp.sort(key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(t) for t in temp]
            