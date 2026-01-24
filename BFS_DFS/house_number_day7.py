#[State]
#[Input] 지도의 크기 
#[Logic] #상하좌우, 있으면 1, 없으면 0

from collections import deque

def solution(n, graph):
    window = [(0,1),(0,-1),(1,0),(-1,0)]
    viliage_total = 0
    vilage_count = []
    ## count, 개수 
    queue = deque()
    for i in range(n):
        for j in range(n):
            count = 0 
            if graph[i][j] == 1:
                queue.append((i, j))
                graph[i][j] = 0
                viliage_total += 1
                count += 1

                while queue :
                    a, b = queue.popleft()
                    for x, y in window:
                        na, nb = a + x, b + y
                        if 0 <= na < n and 0 <= nb < n and graph[a+x][b+y] == 1: #조건 체크가 빠짐. 
                            queue.append((a+x, b+y))
                            graph[a+x][b+y] = 0
                            count += 1
                vilage_count.append(count)

    return viliage_total, sorted(vilage_count)
    #[Output] 단지수 출력, 집의 수 오름차순 출력  



 
from io import StringIO
import sys

testIo = """7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
sys.stdin = StringIO(testIo)

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)] # 이게 왜 틀린건지, 왜 하나는 그냥 형변환을 해야하는지 
print(solution(n, graph))