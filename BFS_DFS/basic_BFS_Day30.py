from io import StringIO
from collections import deque, defaultdict
import sys
#[State] deque
#[Input] 정점 개수, 간선 개수, begin , 간선 연결 정보 
#[Logic]  정점 번호가 작은 것을 먼저 방문 (BFS)
#간선 연결 함수 
#dict vs list 
# visited_list = set()
# queue = deque()
#begin 넣고 
#while queue > 0 
#[Output] 결과 

def solution(begin, node_dict):
    visited_list = set()
    queue = deque()
    queue.append(begin)
    visited_list.add(begin)
    while len(queue) > 0:
        now = queue.popleft()
        print(now, end=" ")
        for i in node_dict[now]:
            if i not in visited_list:
                queue.append(i)
                visited_list.add(i)
    
testI0 = """4 5 1
1 2
1 3
1 4
2 4
3 4
"""
#input print x, testIo는 sys.stdin 으로 받아야함. 
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

solution(begin, node_dict)