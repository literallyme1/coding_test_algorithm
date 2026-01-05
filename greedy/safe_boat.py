#[State] 
#[Input]몸무게를 담은 배열 people, <= 50000 구명보트의 무게 제한 limit 40 <= kg <= 240 -> 240까지 제한 가능 
#[Logic]  무게 제한 a + b <= limit, 최대 2명 
# 구명 보트 적게 사용 방법 
# topointer
#[Output] return boat_count


def solution(people, limit):
    #정렬
    people.sort()
    boat_count = 0
    left =0 
    right = len(people) -1

    while left <= right: # = 이콜도 포함하는 이유는? 
        if (limit - people[right]) >= people[left]: # 알 것 같은데 아직은 이게 맞나 싶음. 
                left += 1
        right -= 1
        boat_count +=1 
    
    return boat_count


print(solution([70, 80, 50], 100))
