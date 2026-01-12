#[State]
#[Input] 1<= people <= 50000, limit
#[Logic] # Greedy 1. 모든 경우 -> 최대한 적게 2. 정렬 필요 3. 현재 선택 최적 
#1. 정렬 
#2. left, right -> to pointer while left <= right
    # right 는 무조건 탑승, left 는 가능하면. 

#[OutPut] 구명보트 개수의 최솟값

