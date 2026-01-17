#[State]
#[Input]  0 ≦ cacheSize ≦ 30, cities <= 100,000, 1. cities tolowercase 함수 
#[Logic] LRU ( 자주 쓰는 거 뒤에) hit : 1, miss : 5
# deque(maxlength), if city in deque -> deque remove, add for 문 
#[Output] total_time 

from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 0
    cache_list = deque(maxlen=cacheSize)
    total_time = 0
    for city in cities:
        if city in cache_list:
            total_time += 1
            cache_list.remove(city)
            cache_list.append(city)
            continue
        total_time += 5
        cache_list.append(city)
    return total_time
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))