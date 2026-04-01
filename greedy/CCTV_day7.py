#[State]
#[Input] routes
#[Logic] 
#[Output]
def solution(routes):
    #1. 정렬 
    routes.sort(key= lambda x : x[0])

    #2. cctv 개수 파악 
    count = 0 
    end = -30001
    for r in routes:
        if r[0] > end:
            count += 1 
            end = r[1]
    return count 


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))