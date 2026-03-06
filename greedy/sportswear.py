


# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2


#[State]
#[Input] n : 전체, lost : 도난 당한 학생 번호들, reserve : 여벌 체육복 있음. 
#[Logic]
# 여벌 체육복 -> 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줌 
#  여벌 학생 도난 -> 빌려줄 수 X
# fcfs 
#[Output] 빌릴 수 있는 최대값 

def solution(n, lost, reserve):
    # 여분 0 -> 도둑 맞은 학생 
    # for i in lost:
    #     if i in reserve:
    #         lost.remove(i)
    #         reserve.remove(i)
    s_lost = set(lost)
    s_reverse = set(reserve)

    intersect = s_lost & s_reverse
    s_lost = s_lost - intersect
    s_reverse = s_reverse - intersect

    # 적은 순서대로 빌릴 수 있는 걸 빌림. 
    lost = list(s_lost)
    lost.sort()
    borrow = 0 
    for idx in lost:
        if idx - 1 in reserve:
            reserve.remove(idx - 1)
            borrow += 1 
        elif idx + 1 in reserve:
            reserve.remove(idx + 1)
            borrow += 1 
    return n - len(lost) + borrow

print(solution(3,	[3],	[1]))



