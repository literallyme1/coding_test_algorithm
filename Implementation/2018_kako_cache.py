#[State] deque 
#[Input]  캐시 크기(cacheSize)  0 ≦ cacheSize ≦ 30 와 문자열 배열(cities)  <= 100,000, for 문 대소문자 구분X(toLowerCase)
#[Logic] LRU(Least Recently Used)
#if city in deque
    #yes -> pop 맨뒤로 count +=1
    #no -> 일단 넘어감. 
#len(deque) == cacheSize 확인   
    #yes : count += 5, deque 넣기 
    #no : left_pop , 뒤에 넣기 += 5
# cacheSize == 0 일 때 특수경우 

#[Output]도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력  

from collections import deque
def solution(size, cities):
    total_count = 0
    cache_list = deque(maxlen=size)

    for city in cities:
        if city in cache_list:
            cache_list.remove(city)
            cache_list.append(city)
            total_count += 1
            continue
    
        #다 찼으면 
        if len(cache_list) == size:
            cache_list.popleft()
        total_count += 5
        cache_list.append(city)
    return total_count

            




def input_normalization(cities):
    for city in cities:
        city = city.lower()
    return cities


cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cacheSize = 3
cities = input_normalization(cities)
print(solution(cacheSize, cities))