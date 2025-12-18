from collections import defaultdict
import sys

def solution(edges):

    in_edge = defaultdict(int)
    out_edge = defaultdict(int)

    # 1. in, out 간선 정보 저장
    for i, j in edges:
        out_edge[i] += 1
        in_edge[j] += 1

    
    #2. 노드 파악 
    nodes = set(in_edge.keys()) | set(out_edge.keys())

    #3. 정점 파악 (들어오는 것 0, 나가는 것 2개 이상)
    center = next(x for x in nodes if in_edge[x] == 0 and out_edge[x] >= 2)

    #4. 막대(나가는 간선이 없는(0개) 노드의 수), 8자 파악 (들어오는 게 2개 이상이면서 "나가는 것도 2개"인 노드)
    bar = sum(1 for x in nodes if x != center and out_edge[x] == 0)
    eight = sum(1 for x in nodes if x != center and in_edge[x] >= 2 and out_edge[x] == 2)
    donut = out_edge[center] - bar - eight

    return [center, donut, bar, eight]
    

edges = eval(input(sys.stdin.readline))
print(solution(edges))