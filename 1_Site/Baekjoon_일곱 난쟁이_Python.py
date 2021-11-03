# list에서 remove 사용시 index를 사용하여 무언가하지 말기!!

array = [int(input()) for i in range(9)]
total = sum(array) - 100

for i in range(9) :
    for j in range(i+1,9) :
        if array[i] + array[j] == total :
            n,m = array[i], array[j]
            array.remove(n)
            array.remove(m)
            break
    if len(array) == 7 :
        break
            
array.sort()
for i in range(7) :
    print(array[i])