#[State]
#[Input]  0 ≦ cacheSize ≦ 30, cities <= 100,000, 1. cities tolowercase 함수 
#[Logic] LRU ( 자주 쓰는 거 뒤에) hit : 1, miss : 5
# deque(maxlength), if city in deque -> deque remove, add for 문 
#[Output] total_time 

def solution(cacheSize, cities):
    return 
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))