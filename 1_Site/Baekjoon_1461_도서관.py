import sys

input = sys.stdin.readline
global result

N,M = map(int, input().rstrip().split())
books = list(map(int, input().rstrip().split()))
negative, positive = [], []
result = 0

for book in books :
    if book < 0 :
        negative.append(abs(book))
    else :
        positive.append(book)

negative.sort()
positive.sort()

if len(negative) == 0 :
    result += positive[-1]
    positive = positive[:-M]
elif len(positive) == 0 :
    result += negative[-1]
    negative = negative[:-M]
else :
    if negative[-1] > positive[-1] :
        result += negative[-1]
        negative = negative[:-M]
    elif positive[-1] > negative[-1] :
        result += positive[-1]
        positive = positive[:-M]
    else :
        if len(positive) > len(negative) :
            result += positive[-1]
            positive = positive[:-M]
        else :
            result += negative[-1]
            negative = negative[-M]

def popStack(list) :
    global result
    while list :
        result += (list[-1] * 2)
        list = list[:-M]

popStack(negative)
popStack(positive)
print(result)

            
