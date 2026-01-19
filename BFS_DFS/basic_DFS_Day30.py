from io import StringIO
import sys
sys.recursionLimit(10**6)
#[State] 재귀
#[Input] 정점 개수, 간선 개수, begin , 간선 연결 정보 
#[Logic] 정점 번호가 작은 것을 먼저 방문 (BFS)

def dfs(visited_list, node_dict):

    for i in node_dict.values():
        if i not in visited_list:
            visited_list.add(i)
            dfs(visited_list, node_dict)



#[Output] 결과 



