def search(array, target, start, end) :
    if start > end :
        return "no"
    mid = (start+end)//2

    if array[mid] == target :
        return "yes"
    elif array[mid] > target :
        return search(array, target,start, mid-1)
    else :
        return search(array, target, mid+1, end)
    


n = int(input())
n_list = list(map(int,input().split(' ')))

m = int(input())
m_list = list(map(int,input().split(' ')))

n_list.sort()

for i in m_list :
    print(search(n_list, i, 0, len(n_list)), end = ' ')