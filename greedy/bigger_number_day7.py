
#[State] deque 
#[Input] number, k 
#[Logic] k 개 제거시 얻을 수 있는 가장 큰 숫자
# 현재 보다 작을 시 이전 것 다 지움.  (가장 처음이 큰게 중요) 지울 시 k 횟수도 같이 지움. 

#[Output] 만들 수 있는 가장 큰 수 -> 문자열

def solution(number, k):
    number = list(map(int, number))
    now = -1 
    queue = []
    for num in number:
        if num > now: # 이전보다 현재가 큼  ##3. now : 끝만 확인 x,  계속 앞전이 나보다 큰지 확인해야 함. queue[-1]
            #작을 시 지우기 
            while queue and k > 0: ## 틀린것 2. 1 이 아니라 0보다 클 때가 되야 0까지 제거 됨. 
                queue.pop()
                k -= 1
        queue.append(num)
        now = num 
    
    ## 1. 틀린 것 
    if k > 0 :
        queue = queue[:-k] # 뒤에서 남은 만큼 제거 

    return "".join([str(i) for i in queue])
            


print(solution("1924",	2))
