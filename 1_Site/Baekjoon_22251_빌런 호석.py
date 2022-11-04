import sys

input = sys.stdin.readline
numbers = [
    [True, True, True, True, True, True, False],
    [False, True, True, False, False, False, False],
    [True, True, False, True, True, False, True],
    [True, True, True, True, False, False, True],
    [False, True, True, False, False, True, True],
    [True, False, True, True, False, True, True],
    [True, False, True, True, True, True, True],
    [True, True, True, False, False, False, False],
    [True, True, True, True, True, True, True],
    [True, True, True, True, False, True, True]    
]
global answer
N,K,P,X = map(int, input().rstrip().split())
answer = 0

def reverseLED(origin, change) :
    result = 0
    for i in range(7) :
        if numbers[origin][i] != numbers[change][i] :
            result += 1

    return result

digits = [0] * (K)
for i in range(K) :
    digits[i] = X % 10
    X //= 10
    if X == 0 :
        break

def getValue(digitList) :
    temp = 0
    for i in range(len(digitList)) :
        temp += (digitList[i] * (10 ** i))
    return temp
    
    
# 반전 한 자릿수, 반전 가능한 갯수, 현재 값
def changeDigit(cnt, inversions, digitList) :
    global answer
    if cnt == K :
        answer += 1
        print(getValue(digitList))
        return

    for i in range(10) :
        if i == digits[cnt] :
            changeDigit(cnt+1, inversions, digitList[:])
        
        else :
            cost = reverseLED(digits[cnt], i)
            if cost > inversions :
                continue
            tempList = digitList[:]
            tempList[cnt] = i
            temp = getValue(tempList)
            if temp > N :
                continue
            changeDigit(cnt+1, inversions - cost, tempList[:])

changeDigit(0, P, digits[:])
print(answer - 1)
            
    
    