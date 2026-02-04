#[State] heap 
#[Input] scoville	K	return
#[Logic] 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
#total = 0 
# while  heap[0] < k and len(heap) >= 2 :
# pop + pop * 2 -> k 에 도달하는 지 if 문 -> 안되면 
#[pop 하기 전에 ]if len(heap) >= 1 인지 확인 하고 될 때까지  pop 조건 만족 x -1 
#total +=1 
#[Output] 섞어야 하는 횟수 return 

