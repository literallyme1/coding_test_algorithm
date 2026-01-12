
#[Input] 그래프의 간선 정보를 담은 2차원 정수 배열 edges, 단방향 edge
    # edges의 원소는 [a,b] 형태이며, a번 정점에서 b번 정점으로 향하는 간선
    #1. in_list, out_list = [ 빈리스트 개수? ]
    #2. 들어오는 것, 나가는 것 각각 넣기 

#[State]
#[Logic] 
   #도넛 모양 : edge = node 개수,  n-1개의 정점들을 한 번씩 방문한 뒤 원래 출발했던 정점으로 돌아옴
   #막대 모양 : node = edge - 1, -1개의 정점을 한 번씩 방문하게 되는 정점이 단 하나
   # 8자 모양 그래프 : node : 홀수, edge : (짝수) edge = node + 1, 2개의 도넛 모양 그래프에서 정점을 하나씩 골라 결합시킨 형태
    # 임의의 간선 생성 -> 도넛과 연결 
    # 정점의 번호와 정점을 생성하기 전 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수
  #1. 중심 쟁점 찾기 (list 가 없는 거)
    # if(in X , out 두개 이상) ==0 center
    # center 에서 out 한 노드 in out 확인 
    # if out 0, in X -> 막대
    # if in, out 개수가 동일, 2개 이상 -> 8자 
    # 외 donut center out len - 막대 - 8자 


#[Output] [생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수]
from collections import defaultdict

def solution(edges):

  in_nodes = defaultdict(list)
  out_nodes = defaultdict(list)
  #노드, 간선 파악 
  for [i, j] in edges:
    in_nodes[j].append(i)  #TypeError: 'builtin_function_or_method' object is not subscriptable => 함수(메서드)를 리스트처럼 [ ] 로 접근했다 => in_nodes[i].append(j)
    out_nodes[i].append(j)
  
  nodes = set(out_nodes.keys()) #in_node 가 아니라 out 을 가져왔어야 
  center = -1
  total = 0
  #쟁점 파악 (개수 알 수 있음.)
  for node in nodes:
    if len(out_nodes[node]) >= 2 and len(in_nodes[node]) == 0:
        center =  node 
        total = len(out_nodes[node])
  
  stick = 0
  eight = 0
  donut = 0
  for node in nodes:
    if len(in_nodes[node]) == 1 and len(out_nodes[node]) == 0:
        stick += 1
    elif len(in_nodes[node]) >= 2 and len(out_nodes[node]) == 2:
       eight += 1 
  
  donut = total - stick - eight

  return [center, donut, stick, eight]
    # 가능?
  # for [a, b] in edges:
  #    in_list



print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
  


