#[State] list
#[Input] begin	target	words
#[Logic]  begin -> target 으로 최소 변환 

#최단거리 
#1. 하나만 달라지는 거 찾음. 큐 
#2 queue 에 cog 가 있으면 중지. 없으면 반복 
#3. vistied 가 필요할까?  필요 없을 듯 
#4. 조건 이 있어서 이걸 어떻게 다뤄야 하지 => dict count(int) : []

# for word in words:
#word 별로 target 이 나오는 최단 경로 찾음 = bfs 
    # if  begin + word => len(set) == 1 => 큐 
        #count +=1 
    # if target in queue과 같으면 종료 -> 리스트에 넣어놓음. 

# return  max(최단거리 리스트)

#[Output] 최소 변환 count

#틀린점
#count 위치 -> 큐에 튜플 넣기 
# set 순서 고려 X -> zip 으로 비교 
#visitedlist 필요함. 
