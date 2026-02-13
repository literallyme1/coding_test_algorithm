
#[State] BFS 
#[Input] begin	target	words
#[Logic]
#1. target 단어가 있는 지 확인 
#2. visited_list = sort() depth 와 같이 tuple 로 넣기 
#3. begin 넣기 
#while visited_list:
# zip 다른게 하나 true  (함수)
# true 일 시 넣기 
# if target 이 나오면 종료 total
#[Output]

#1. 한 선택지가 sort 요소에 있는대로 만 갈 수 있는 거 카운트  x -> 어차피 반복 
#2. 각각 depth 가 다른 걸 걱정? => 리스트가 하나 각각 분리가 필요 