n = int(input())
student = dict()

for _ in range(n) :
    key, value = input().split()
    value = int(value)
    student.setdefault(key,value)

max_value = max(student.values())+1

# 얕은 복사 : 단순히 이 방법으로 배열을 선언하게 되면 요소를 복사하는 얕은 복사가 일어난다.
# 즉, 이러한 방식으로 리스트를 선언 후에 값을 변경하게 되면 다른 원소들의 값도 변경되는 현상이 발생하므로 이를 인지하여 사용하여야 한다.
#temp = [[]] * max_value
temp = [[] for i in range(max_value)]

for i in student :
    temp[student.get(i)].append(i)

for i in temp :
    while i :
        print(i.pop(), end = ' ')

