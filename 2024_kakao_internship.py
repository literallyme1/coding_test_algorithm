
#input
from collections import defaultdict, Counter
import sys 

edge_dict = defaultdict(list)
edge_num_dict = defaultdict(int)
edge_list = eval(sys.stdin.readline())
print(edge_list)


#간선 정보 획득
for i in edge_list:
    edge_dict[i[1]].append(i[0])
    edge_num_dict[i[1]] += 1

print(edge_num_dict.items())



#정점 찾기

#center 는 엣지가 하나도 없는 것이 해당. 
# 어떻게 얻을 지는 고민 

# 연관관계 파악

for i in edge_num_dict:
