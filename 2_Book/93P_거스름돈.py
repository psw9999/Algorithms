
coin = [500,100,50,10]
cnt = 0
money = input("거스름돈을 입력하세요.")
money = int(money)

for i in coin :
    if i <= money :
        cnt += money//i
        money = money%i
        if money == 0 : 
            break
