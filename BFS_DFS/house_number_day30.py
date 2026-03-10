from io import StringIO
import sys
from collections import deque


def solution(n, graph):
    # return 총 단지수, 오름차순 집의 수 쓰기 
    queue = deque()
    total_house =0
    house_list = []
    # index 로 접근 
    for row in range(n):
        for column in range(n):
            if graph[row][column] == 1:
                house_num = 1
                total_house += 1
                #넣기
                queue.append((row, column))
                graph[row][column] = 0
                r_v = [1,-1,0,0]
                c_v = [0,0,1,-1]
                while queue:
                    n_r, n_c = queue.pop()
                    #상하좌우를 볼꺼임. 범위 안넘으면
                    for i in range(4):
                        c_r = n_r + r_v[i]
                        c_c = n_c + c_v[i]
                        if 0 <= c_r < n and  0 <= c_c < n and graph[c_r][c_c]:
                            queue.append((c_r, c_c))
                            graph[c_r][c_c] = 0
                            house_num += 1
                house_list.append(house_num)
    print(total_house)
    house_list.sort()
    for house in house_list : print(house) 

                    

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
graph = [list(map(int, input())) for _ in range(n)]

solution(n, graph)

