# # 이진 탐색
# import sys
# input = sys.stdin.readline

# def BST(weight) :
#     global jewelry, case
#     left, right = 0, len(jewelry)-1
#     mid = (left + right) // 2
#     while left <= right :
#         if weight == jewelry[mid][0] :
#             return mid
#         if weight > jewelry[mid][0] :
#             left = mid + 1
#         elif weight < jewelry[mid][0] :
#             right = mid - 1
#         mid = (left + right) // 2
#     return mid

# N,K = map(int,input().rstrip().split())

# jewelry = []
# case = []

# # m : 무게, v : 가격
# for _ in range(N) :
#     tm,tv = map(int,input().rstrip().split())
#     jewelry.append([tm,tv])
# jewelry.sort()

    
# for _ in range(K) :
#     case.append(int(input().rstrip()))
# case.sort()

# result = 0
# for k in case :
#     index = BST(k)
#     maxV = 0
#     temp = -1
#     for i in range(index+1) :
#         if maxV < jewelry[i][1] :
#             maxV = jewelry[i][1]
#             temp = i
#     jewelry[temp][1] = -1
#     result += maxV
# print(result)

# 우선순위 큐
import sys
import heapq
input = sys.stdin.readline

N,K = map(int,input().rstrip().split())

jewelry = []
case = []

# m : 무게, v : 가격
for _ in range(N) :
    tm,tv = map(int,input().rstrip().split())
    jewelry.append((tm,tv))
jewelry.sort(reverse= True)

# 가방   
for _ in range(K) :
    case.append(int(input().rstrip()))
case.sort()

heap = []
result = 0
for k in case :
    while jewelry :
        m,v = jewelry[-1]
        if k >= m :
            m,v = jewelry.pop()
            heapq.heappush(heap,-v)
        else :
            break

    if len(heap) > 0 :
        result -= heapq.heappop(heap)
    
print(result)