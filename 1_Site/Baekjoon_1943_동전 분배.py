import sys

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
    
    if (sumAmount % 2) != 0 :
        continue
    
    target = sumAmount // 2
    dp = [0] * (target+1)
    dp[0] = 1
    
    for price, count in coins :
        if result[r] :
            break
        
        for i in range(target, price-1, -1) :
            if result[r] :
                break

            if dp[i-price] :
                for c in range(count) :
                    temp = i+(price*c)
                    if temp < target :
                        dp[temp] = 1
                    elif temp == target :
                        result[r] = True
                        break
                    else :
                        break

for r in result :
    if r :
        print(1)
    else :
        print(0)
