#[State]
#[Input] routes (차량이 들어온 지점, 나간지점 2차원 배열)
#[Logic] 
#[Output] return 다 찍히려면 몇대의 카메라 설치 
# set 안에 set 못넣음. 

def solution(routes):
    rlst = [] # set 초기값 설정 방법
    for route in routes:
        nr = [i for i in range(route[0], route[1]+1)]
        tlst = rlst # 깊은 복사가 되려나? 
        for r in tlst:
            if frozenset(nr) in frozenset(r):
                if(len(nr) > len(r)):
                    mr = set(nr) & set(r)
                else:
                    mr = set(r) & set(nr)
                rlst.remove(r)
                rlst.append(mr)
                nr = -1
                break
        
        if len(nr) != -1:
            rlst.append(set(nr))

    return len(rlst)

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))