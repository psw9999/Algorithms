import re
from collections import defaultdict 
def solution(word, pages):
    word = word.lower()
    webDict = defaultdict(list)
    for i, page in enumerate(pages) :
        page = page.lower()
        
        # 웹의 URL 추출
        temp = page.split("<meta property=\"og:url\" content=")
        temp = temp[1].split("/>")
        URL = temp[0]
        
        # 기본점수
        pattern = re.compile("[^a-z]")
        temp = re.split(pattern, page)
        keyword = temp.count(word)
        
        # 하이퍼링크
        linkList = []
        linkCnt = page.count("<a href=")
        for j in range(1, linkCnt+1) :
            temp = page.split("<a href=")
            temp = temp[j].split(">")
            linkList.append(temp[0])
        
        webDict[URL] = [keyword, linkList, i, 0]
    
    for key, value in webDict.items() :
        cost = value[0]
        linkList = value[1]
        for link in linkList :
            if link not in webDict.keys() :
                continue
            else :
                webDict[link][3] += (cost / len(linkList))

    result = 0
    maxV = 0
    for value in webDict.values() :
        temp = value[0] + value[3] 
        print(temp)
        if maxV < temp :
            maxV = temp
            result = value[2]
    
    return result