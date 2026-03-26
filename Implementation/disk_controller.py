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
    heap = []
    #1. 번호 삽입 -> heap
    for i, (start, time) in enumerate(jobs):
        heapq.heappush(heap, (time, start,  i+1))
    #2. 디스크 가동 
    wlst= []
    total = 0
    for _ in range(len(jobs)):
        time, start, i  = heapq.heappop(heap) # heap 이 우선순위 맞춰 가져옴. 
        end = total + time if total > start else start + time # 프로세스가 들어오는 데까지 휴동시간 생각 x 바로 total + time 으로 함. 
        wait = end - start
        wlst.append(wait)
        total = end 
    return sum(wlst) // len(wlst)




jobs = [[0, 3], [1, 9], [3, 5]]

print(solution(jobs))