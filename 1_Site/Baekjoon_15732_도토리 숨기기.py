import sys

input = sys.stdin.readline
N, K, D = map(int, input().rstrip().split())
DP = [0] * (N+1)

# 각 상자에 몇개의 도토리가 있어야 하는지 대입
for _ in range(K) :
    start, end, distance = map(int, input().rstrip().split())    
    for i in range(start, end+1, distance) :
        DP[i] += 1

boxes = []
sumValue = 0

# 도토리가 담긴 상자만 꺼내오기
for i in range(N+1) :
    if DP[i] != 0 :
        # 인덱스, 갯수
        sumValue += DP[i]
        boxes.append((i, DP[i]))

remainder = (D % sumValue)
if remainder == 0 :
    print(boxes[-1][0])
else :
    for index, cnt in boxes :
        remainder -= cnt
        if remainder <= 0 :
            print(index)
            break
        