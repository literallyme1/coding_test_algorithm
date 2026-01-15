#[State] visited = set(), node, 0
#[Input] 지도 크기 N(정사각형) N 개의 자료 
#[Logic] 좌우상하 모임 정의 -> 단지 번호 
#끝난 건 0, 제일 처음 1이 시작 노드 count 

#vistied_list = set()
#Count = 0
#Count_list = []

#for i in range(n):
    #for j in range(n):
        #if graph[i][j]  == 1:
            #queue = (i, j)
            #while queue > 0:
                #queue.leftpop 
                #if graph[pop1][pop2] == 1
                #visited 에 있는 지 확인 (아래 모두)
                #if   graph[ipop1-1][pop2j] == 1
                #if   graph[i][j+1] == 1
                #if   graph[i][j-1] == 1
                #해당 시, queue , visited 넣기 
            #visited_list len -> count 
            # for i, j in visited_list
                #0만들기 

#BFS 선택이유 -> 붙어있기 때문에 DFS, 겹치는 게 ^ 재귀보단 bfs 가 낫지 않을까?
#[Output] 단지 개수, 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력
# return count_list.sort(), 단지개수 

import sys
from collections import deque
from io import StringIO

# input = sys.stdin.readline


# def update_queue(): #부모를 쓸 수있는 경우 

def solution(n, graph):
    count_list = []
    queue = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                queue.append((i, j))
                count = 0
                while len(queue) > 0:
                    row, col = queue.popleft() 
                    if graph[row + 1][col] == 1: #하
                        queue.append((row + 1, col))
                        graph[row + 1][col] = 0 
                        count += 1

                    if graph[row - 1][col] == 1: #상
                        queue.append((row - 1, col))
                        graph[row - 1][col] = 0
                        count += 1  
                        

                    if graph[row][col - 1] == 1: #좌
                        queue.append((row, col - 1))
                        graph[row][col - 1] = 0  
                        count += 1

                    if graph[row][col + 1] == 1: #우
                        queue.append((row, col + 1))
                        graph[row][col + 1] = 0  
                        count += 1
                count_list.append(count) 

    print(count_list)
    return count_list.sort()

test_input = """7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
sys.stdin = StringIO(test_input)

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)] #sys.stdin 과 이 코드 몰랐음. 
print(solution(n, graph))

