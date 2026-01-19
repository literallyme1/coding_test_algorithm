from io import StringIO
import sys
sys.recursionLimit(10**6)
#[State] 재귀
#[Input] 정점 개수, 간선 개수, begin , 간선 연결 정보 
#[Logic] 정점 번호가 작은 것을 먼저 방문 (BFS)
#[Output] 결과 