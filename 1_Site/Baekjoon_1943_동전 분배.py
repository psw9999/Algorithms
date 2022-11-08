import sys
import heapq

input = sys.stdin.readline
result = [False, False, False]
for r in range(3) :
    N = int(input().rstrip())
    coins = []
    sumAmount = 0
    
    for _ in range(N) :
        price, count = map(int, input().rstrip().split())
        coins.append((price, count))
        sumAmount += (price * count)
    
    # 합계가 홀수라면 탈출
    if sumAmount %2 != 0 :
        #print(0)
        continue

    target = sumAmount // 2
    coins.sort(reverse=True)
    queue = []
    
    for cnt in range(1, coins[0][1]+1) :
        price = coins[0][0] * cnt
        if target >= price :
            heapq.heappush(queue, (price, 0))
        else :
            break
        
    flag = False
    while queue :
        price, index = heapq.heappop(queue)
        if price == target :
            flag = True
            break
        
        if (index+1) >= len(coins) :
            continue
            
        for i in range(index+1, len(coins)) :
            coin_price = coins[i][0]
            for cnt in range(1, coins[i][1]+1) :
                temp = price + (coin_price * cnt)
                
                if temp >= price :
                    heapq.heappush(queue, (temp, i))
                
                else :
                    break
        
    if flag :
        result[r] = True

for r in result :
    if r :
        print(1)
    else :
        print(0)
    

    
    
        