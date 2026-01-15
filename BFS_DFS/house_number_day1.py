#[State] visited = set(), node, 0
#[Input] 지도 크기 N(정사각형) N 개의 자료 
#[Logic] 좌우상하 모임 정의 -> 단지 번호 
#끝난 건 0, 제일 처음 1이 시작 노드 count 

#vistied_list = set()
#Count = 0
#Count_list = []
#queue = (i, j)
#for i in range(n):
    #for j in range(n):
        #if graph[i][j]  == 1:
            #while queue > 0:
                #queue.leftpop 
                #if graph[i+1][j] == 1
                #visited 에 있는 지 확인 (아래 모두)
                #if   graph[i-1][j] == 1
                #if   graph[i][j+1] == 1
                #if   graph[i][j-1] == 1
                #해당 시, queue , visited 넣기 
            #visited_list len -> count 
            # for i, j in visited_list
                #0만들기 

#BFS 선택이유 -> 붙어있기 때문에 DFS, 겹치는 게 ^ 재귀보단 bfs 가 낫지 않을까?
#[Output] 단지 개수, 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력
# return count_list.sorted()

# import sys
# input = sys.readline

# n = input()
# graph = [ list(input())for i in range(n)]
