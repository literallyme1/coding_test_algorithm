#[State] heap 
import heapq
#[Input] scoville	K	
def solution(scovile, k):
    heapq.heapify(scovile)
    total_mix = 0
    while scovile[0] < k and len(scovile) >= 2:
#[Logic] 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        last_scoville = heapq.heappop(scovile) + (heapq.heappop(scovile) * 2)
        heapq.heappush(scovile, last_scoville)
        total_mix += 1

    return total_mix if len(scovile) > 0 and scovile[0] >= k else -1
#[pop 하기 전에 ]if len(heap) >= 1 인지 확인 하고 될 때까지  pop 조건 만족 x -1 
#total +=1 
#[Output] 섞어야 하는 횟수 return 

