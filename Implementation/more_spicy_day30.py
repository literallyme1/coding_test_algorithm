#[State] heapq 
#[Input]
#[Logic] 가장 낮은 두개의 음식 섞음 < = K
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# while heapq[0] >= k 

#[Output] return 섞어야 하는 최소 횟수, 못 만들 시 -1 

import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    mix = 0
    while scoville[0] < k:
        if len(scoville) < 2: 
            return -1
        f_1 = heapq.heappop(scoville)
        f_2 = heapq.heappop(scoville)
        mix_sco = f_1 + f_2 * 2 
        #종료 조건 
        heapq.heappush(scoville, mix_sco)
        mix += 1 
    return mix

print(solution([1, 2, 3, 9, 10, 12],	7))

    