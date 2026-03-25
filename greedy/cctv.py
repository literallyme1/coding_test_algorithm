#[State]
#[Input] routes (차량이 들어온 지점, 나간지점 2차원 배열)
#[Logic] 
#[Output] return 다 찍히려면 몇대의 카메라 설치 
# set 안에 set 못넣음. 

def solution(routes):
    routes.sort(key = lambda x : x[1])
    last = - 30001
    camera = 0 
    for s, e in routes:
        if s > last:
            camera += 1
            last = e


    return camera

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))