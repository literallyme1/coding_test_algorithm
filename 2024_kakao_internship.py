
from collections import defaultdict

def solution(edges):
    #들어오는 간선
    indeg = defaultdict(int)
    #나가는 간선
    outdeg = defaultdict(int)

    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1

    nodes = set(indeg.keys()) | set(outdeg.keys())

    #정점 (들어오는 간선 0, 나가는 간선 2개 이상)
    center = next(x for x in nodes if indeg[x] == 0 and outdeg[x] >= 2)

    # 제너레이터 ( x for x in list if 조건문 -> 제일 앞 bool, value 변형 가능, bool 일 때 true 일 시 1)
    bar = sum(outdeg[x] == 0 for x in nodes if x != center)
    eight = sum(indeg[x] >= 2 for x in nodes if x != center)

    donut = outdeg[center] -  bar - eight

    return [center, donut, bar, eight]




