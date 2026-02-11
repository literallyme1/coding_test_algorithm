#[State] 
import heapq

#[Input] scoville	K

def solution(scoville, K):
    heapq.heapify(scoville)
    total = 0
#[Logic]
    while scoville[0] < K and len(scoville) > 1:
        new_scovile = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_scovile)
        total += 1
    return total if scoville[0] >= K else -1


#  섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
#[Output] 섞어야 하는 최소 횟수를 return, 없는 경우 -1을 return 

print(solution([1, 2, 3, 9, 10, 12],	7))