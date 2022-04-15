def columnCheck(x,y) :
    global columnGraph, beamGraph,N
    # 바닥 위
    if y == 0 :
        return True
    # 보의 한쪽 끝(왼쪽)
    if beamGraph[y][x] == 1 :
        return True
    # 보의 한쪽 끝 (오른쪽)
    if x > 0 and beamGraph[y][x-1] == 1 :
        return True
    # 또 다른 기둥의 위
    if y > 0 and columnGraph[y-1][x] == 1 :
        return True
    return False

def beamCheck(x,y) :
    global columnGraph, beamGraph,N
    # 한쪽 끝이 기둥 (왼쪽)
    if columnGraph[y-1][x] == 1 :
        return True
    # 한쪽 끝이 기둥 (오른쪽)
    if x < N and columnGraph[y-1][x+1] == 1 :
        return True
    # 양쪽 끝이 다른 보와 동시에 연결
    if (x > 0 and beamGraph[y][x-1]) and (x < (N-1) and beamGraph[y][x+1]) :
        return True
    return False

def solution(n, build_frame):
    global columnGraph, beamGraph,N
    N = n
    columnGraph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    beamGraph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for x,y,kind,install in build_frame : 
        # 기둥 + 설치
        if kind == 0 and install == 1 :
            if columnCheck(x,y) :
                columnGraph[y][x] = 1

        # 보 + 설치
        elif kind == 1 and install == 1 :
            if beamCheck(x,y) :
                beamGraph[y][x] = 1
                
        # 기둥 + 해체
        elif kind == 0 and install == 0 :
            columnGraph[y][x] = 0
            
            # 왼쪽 보 체크
            if x > 0 and beamGraph[y+1][x-1] == 1 :
                if not beamCheck(x-1,y+1) :
                    columnGraph[y][x] = 1
                    continue
            
            # 오른쪽 보 체크
            if beamGraph[y+1][x] == 1 :
                if not beamCheck(x,y+1) :
                    columnGraph[y][x] = 1
                    continue
            
            # 위쪽 기둥 체크
            if y < N and columnGraph[y+1][x] == 1 : 
                if not columnCheck(x,y+1) :
                    columnGraph[y][x] = 1
                    continue
        
        # 보 + 해체
        elif kind == 1 and install == 0 :
            beamGraph[y][x] = 0
            
            # 왼쪽 보 체크
            if x > 0 and beamGraph[y][x-1] == 1 :
                if not beamCheck(x-1,y) :
                    beamGraph[y][x] = 1
                    continue
            # 오른쪽 보 체크
            if x < (N-1) and beamGraph[y][x+1] == 1 :
                if not beamCheck(x+1,y) :
                    beamGraph[y][x] = 1
                    continue
            # 왼쪽 위 기둥 체크
            if columnGraph[y][x] == 1 :
                if not columnCheck(x,y) :
                    beamGraph[y][x] = 1
                    continue
            # 오른쪽 위 기둥 체크
            if x < N and columnGraph[y][x+1] == 1 :
                if not columnCheck(x+1,y) :
                    beamGraph[y][x] = 1
                    continue
    
    result = []
    for x in range(N+1) :
        for y in range(N+1) :
            if columnGraph[y][x] == 1 :
                result.append((x,y,0))
            if beamGraph[y][x] == 1 :
                result.append((x,y,1))
    
    return result