from io import StringIO
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
#[State] 재귀
#[Input] 정점 개수, 간선 개수, begin , 간선 연결 정보 
#[Logic] 정점 번호가 작은 것을 먼저 방문 (BFS)

def dfs(visited_list, node_dict, now):
    print(now, end=" ")
    for i in node_dict[now]:
        if i not in visited_list:
            visited_list.add(i)
            dfs(visited_list, node_dict, i)



#[Output] 결과 


testI0 = """4 5 1
1 2
1 3
1 4
2 4
3 4
"""

sys.stdin = StringIO(testI0)
node, line, begin = map(int, input().split())
node_dict = defaultdict(list)
for _ in range(line) :
    n1, n2 = map(int, input().split())
    node_dict[n1].append(n2)
    node_dict[n2].append(n1)
#dict 로 한다면 sort 는 어떻게 하지? 
for key, value in node_dict.items():
    node_dict[key] = sorted(value)
visited_list = set()
visited_list.add(begin)
dfs(visited_list, node_dict, begin)

