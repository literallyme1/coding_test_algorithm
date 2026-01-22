#[State]
#[Input] 지도의 크기 
#[Logic] #상하좌우, 있으면 1, 없으면 0

from collections import deque
window = [(0,1),(0,-1),(1,0),(-1,0)]

## count, 개수 
queue = deque()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))
            graph[i][j] = 0
            while queue :
                a, b = queue.popleft()
                for x, y in window:
                    if graph[a+x][b+y] == 1:
                        queue.append((a+x, b+y))
                        graph[a+x][b+y] = 0

return 
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
graph = [map(int, list(input()))for _ in range(7)] # 이게 왜 틀린건지, 왜 하나는 그냥 형변환을 해야하는지 