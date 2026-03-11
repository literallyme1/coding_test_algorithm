#[State] 앞에서 부터 주는 게 최선의 선택 
#[Input] n, lost, reserve
#[Logic]

# 앞 or 뒤 빌려줄 수 0
#[Output] 수업 가능 학생 최대값 

def solution(n, lost, reverse):
    s_lost = set(lost)
    s_reverse = set(reverse)

    # 1. reserve 학생이 도난 당했을 가능성
    intersect = s_lost & s_reverse
    s_lost -= intersect
    s_reverse -= intersect

    # 2. 왼 -> 오 순 우선순위
    for i in range(1, n):
        if i in s_lost:
            if i - 1 > 0 and i - 1 in s_reverse:
                s_lost.remove(i)
                s_reverse.remove(i - 1)
            
            elif i + 1 <= n and i + 1 in s_reverse:
                s_lost.remove(i)
                s_reverse.remove(i + 1)
            

    return n - len(s_lost)

print(solution(5,	[2, 4],	[1, 3, 5]))
