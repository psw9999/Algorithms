
import sys

input = sys.stdin.readline

N = int(input())

def calcul(t,sm,ss,em,es) :
    global team_list
    t-=1
    tm = em - sm
    if es < ss :
        tm -= 1
        es += 60
    ts = es - ss
    team_list[t][0] += tm
    team_list[t][1] += ts

team_list = [[0,0],[0,0]]
stack = []

for _ in range(N) :
    team, time = input().rstrip().split()
    team = int(team)
    m,s = map(int, time.split(":"))
    
    if stack :
        if team != stack[-1][0] :
            tt, tm, ts = stack.pop()
            if not stack :
                calcul(tt,tm,ts,m,s)
        else :
            stack.append((team,m,s))
    else :
        stack.append((team,m,s))

if stack :
    dt,dm,ds = stack[0]
    calcul(dt,dm,ds,48,00)

for dm,ds in team_list :
    dm = (ds//60) + dm
    ds = (ds%60)
    if dm < 10 :
        dm = "0" + str(dm)
    if ds < 10 :
        ds = "0" + str(ds)
    print(str(dm) + ":" + str(ds))


