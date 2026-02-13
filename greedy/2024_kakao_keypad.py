#[State]
#[Input] numbers, hand 
def solution (numbers, hand):
    # graph = [[ row * 3 + i for i in range(1, 4)] for row in range(0, 3)]
    # 인덱스값 -> 딕셔너리?
    index_dic = {}
    for row in range(0, 4):
        for i in range(0, 3):
            index_dic[row * 3 + (i+1) ] = (row, i)

    #hand 고치기 
    if hand == "right":
        hand = "R"
    else:
        hand = "L"

    left_loc, right_loc = 10, 12
    result = ""
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            result += "L" #add 함수도 가능한가?
            left_loc = num
        elif num == 3 or num == 6 or num == 9:
            result += "R"
            right_loc = num
        else:
            if num == 0:
                num = 11
            
            #num 거리 구하기 
            r1, c1 = index_dic[num]

            # L 거리 구하기
            r2, c2 = index_dic[left_loc]
            left_distance = abs(r1 - r2) + abs(c1 - c2)
            # R 거리 구하기 
            r2, c2 = index_dic[right_loc]
            right_distance = abs(r1 - r2) + abs(c1 - c2)
            if left_distance > right_distance:
                result += "L"
                left_loc = num
            elif left_distance < right_distance:
                result += "R"
                right_loc = num
            else:
                result += hand
                if hand == "L":
                    left_loc = num
                else:
                    right_loc = num 
    return result


#[Logic] 
# left_loc, right_loc
#if 문 
# 1, 4, 7 -> 왼손 add L
# 3, 6, 9 -> 오른손 add R
# 2, 5, 8,  -> 우선순위 
#   1. 위치에 가까움 1, -1 or 3, - 3 해당하는 지 둘 다 있으면  hand 에 해당 // 4 r기준 -> 좌표가 더 나음.
# |r1 - r2| + |c1 - c2| 
#   2. 0일 시 8 치환 

#[Output] "LRLLLRLLRRL"

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"))