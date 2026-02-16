#[State] Deque 
#[Input]cacheSize, cities
from collections import deque
def solution(cacheSize, cities):

    n = len(cities)
    hit, miss = 1, 5

    cities = [city.lower() for city in cities]

    if cacheSize == 0:
        return n * miss
    
    lru = deque(maxlen= cacheSize)

    total = 0
    for city in cities:
        if city in lru:
            total += hit
            lru.remove(city)
        else:
            total += miss
        lru.append(city)
    
    return total

    

#[Logic] 
#total = 0 
# 1. 전처리 
# 2. cacheSize = 0 -> len * 5
# 3. if 문, 있으면 hit , or miss 
# 4. size 있는 deque -> add 
#[Output] total 
print(solution(3,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

