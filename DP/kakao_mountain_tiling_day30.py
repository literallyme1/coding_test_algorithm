#[State]
#[Input] n	tops
#[Logic] 

"""
침범 여부

top 0 
현재 침범 : 이전 침범  1
현재 침범 : 이전 침범 x 1 
현재 침범x : 이전 침범 2
현재 침범 x: 이전 침범 x 3

top x
현재 침범 : 이전 침범  1
현재 침범 : 이전 침범 x 1
현재 침범x : 이전 침범 1
현재 침범 x: 이전 침범 x 2
"""

def solution(n, tops):
    intrude = 0
    not_intrude = 1

    for i in range(n):
        temp_intrude = intrude
        temp_not_intrude= not_intrude
        if tops[i] == 0:
            intrude = temp_intrude + temp_not_intrude
            not_intrude = temp_intrude + temp_not_intrude * 2
        else:
            intrude = temp_intrude + temp_not_intrude
            not_intrude = temp_intrude * 2 + temp_not_intrude * 3

    return intrude + not_intrude

print(solution(4, [1, 1, 0, 1]))