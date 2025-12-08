
def solution(n, tops):
    #1. 리스트 X -> 2개 값만 쓰므로 기억 할 필요 X
    intrude, not_intrude = 1, 3 if tops[0] else 2
    division = 10007

    #2. 정보 수집 
    for i in range(2, n + 1):
        if tops[i - 1] == 0:
            new_intrude = intrude + not_intrude
            new_not = intrude + 2 * not_intrude
        else:
            new_intrude = intrude + not_intrude
            new_not = 2 * intrude + 3 * not_intrude

        intrude = new_intrude % division
        not_intrude = new_not % division


    return (intrude + not_intrude) % division


print(solution(4, [1, 1, 0, 1]))


"""
def solution(n, tops):
    #1. DP 저장 할 리스트 생성
    intrude_list = [0] * (n + 1)
    not_intrude_list = [0] * (n + 1)
    division = 10007

    #2. 첫 값 
    intrude_list[1] = 1
    not_intrude_list[1] = 3 if tops[0] == 1 else 2 

    #3. 정보 수집 
    for i in range(2, n+1):

        #현재 역삼각형이 침범한 경우 
        intrude_list[i] = intrude_list[i-1] + not_intrude_list[i-1]  
        #현재 역삼각형이 침범하지 않은 경우(삼각형, top 마름모, 침범 X 마름모)
        not_intrude_list[i] = intrude_list[i-1] + 2 * not_intrude_list[i - 1] if tops[i - 1] == 0 else 2 * intrude_list[i - 1] + 3 * not_intrude_list[i - 1]


    return (intrude_list[n] % division + not_intrude_list[n] % division) % division


print(solution(4, [1, 1, 0, 1]))

"""


