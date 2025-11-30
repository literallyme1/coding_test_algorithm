from collections import defaultdict

def solution(edge_list):

    #1. 간선 세기(defaultInt)
    out_edge = defaultdict(int)
    in_edge = defaultdict(int)

    for a, b in edge_list:
        out_edge[a] += 1
        in_edge[b] += 1
    
    nodes = set(list(in_edge.keys()) + list(out_edge.keys()))
    #2. center 찾기 (나가는 선 1 초과)
    center = next(x for x in iter(nodes) if out_edge[x] > 1 and in_edge[x] == 0)
    print(center)

    #3. 그래프 세기
    #3-1. 나가는 거 x (막대)
    stick = sum (1 for x in iter(nodes) if out_edge[x] == 0 and x != center)
    #3-2. 나가는거 = 들어오는 거, 2개 이상 (8자)
    eight = sum(1 for x in iter(nodes) if out_edge[x] >= 2 and in_edge[x] >= 2 and x != center)
    # center.out - (막대 + 8자)
    donut = out_edge[center] - stick - eight
    return [center, donut, stick, eight]



result = solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])
print(result)