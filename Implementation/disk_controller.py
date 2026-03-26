#[State] 반환시간lst, heap() 넣기 
#[Input] 2차원 배열 jobs 
#[Logic] 

# 대기큐 num, request_time, time 
# 우선순위에 따라 진행 time 이 짧음 > 요청 시간 이 빠름 > 작업 번호가 작음 , 비선점 
# 대기시간 = 종료시간 - 요청 시간 
# 종료 시간 = 요청시간 + 작업 시간  

#[Output] return 작업 반환 시간의 평균 

import heapq

def solution(jobs):
    jobs = sorted([(start, time, i) for i, (start, time) in enumerate(jobs)])

    heap = []
    now, i, total_wait = 0, 0, 0
    while i <len(jobs):
        #1. 현재 시점까지 들어온 요청 heap 에 넣음 ( 중복 막기 위해 start 이상)
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, (j[1], j[0], j[2]))
        
        if heap:
            duration, req_time, idx = heapq.heappop(heap)
            start = now 
            now += duration
            total_wait += (now - req_time) #총시간에서 온시간 빼기 
        else:
            now += 1
    return total_wait // len(jobs)


jobs = [[0, 3], [1, 9], [3, 5]]

print(solution(jobs))