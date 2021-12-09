from collections import deque

def solution(begin, target, words):
    visited = {}
    for word in words:
        visited[word] = 0
    queue = deque()
    visited[begin] = 1
    queue.append((begin,0))
    
    while queue :
        curWord,cnt = queue.popleft()
        if curWord == target :
            return cnt
        for word in words :
            wordCnt = 0
            if visited[word] == 0 :
                for i in range(len(word)) :
                    if curWord[i] == word[i] :
                        wordCnt += 1
                        
            if wordCnt == (len(word) - 1) :
                visited[word] = 1
                queue.append((word,cnt+1))
    
    return 0