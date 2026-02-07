#[State] two_pointer
#[Input] people	limit	return
def solution(people, limit):
    n = len(people)
    people.sort()
    right = n -1 
    left = 0 
    total = 0 
    while left <= right : 
        if people[left] + people[right] <= limit:
            left += 1 
        right -= 1
        total += 1
    return total

print(solution([70, 50, 80, 50],	100))

#[Logic] 최대 2명, 무게 제한 0 sort
#구명보트를 최대한 적게 사용하여 모든 사람을 구출 
# 모두 구출, 가장 큰 사람에 작은사람이 탈 수 있는 지 확인 
#total, left, right = len(people) - 1 
# while left <= right:
    #반복 

#[Output] total 