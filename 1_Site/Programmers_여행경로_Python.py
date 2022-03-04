import sys
from collections import defaultdict,deque
sys.setrecursionlimit(10000)

result = []
airports = defaultdict(deque)
N = 0

def trip(arrival,routes) :
    global airports,result, N
    #print(arrival, airports[arrival])
    
    if not airports[arrival] :
        if len(routes) == (N+1):
            result.append(list(routes))
        return routes.pop() 

    else :
        for _ in range(len(airports[arrival])) :
            start = airports[arrival].pop()
            routes.append(start)
            airports[arrival].appendleft(trip(start,routes))
        return routes.pop()

def solution(tickets):
    global N
    N = len(tickets)
    
    for ticket in tickets :
        airports[ticket[0]].append(ticket[1])
    
    temp = deque(["ICN"])
    for _ in range(len(airports["ICN"])) :
        start = airports["ICN"].pop()
        temp.append(start)
        airports["ICN"].appendleft(trip(start,temp))
    
    result.sort()
    return result[0]