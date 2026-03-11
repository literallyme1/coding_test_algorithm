#[State] 
#[Input]  numbers	hand = "left"는 왼손잡이, "right"는 오른손잡이를 의미
#[Logic] 
# 시작점 * #
# 1. 1, 4, 7 -> 왼
# 2. 3, 6, 9 -> 오
#3. 2, 5, 8, 0 -> 더 가까운 거 (좌표 계산), 동일 시 hand 에 따라 


#[Output] result LR "".join

def find_point(num):
    # x 좌표 
    x, y = 0, 0
    if num in ["*", 0, "#"]:
        x = 3 
        if num == "*":
            y = 0
        elif num == 0:
            y = 1
        else:
            y = 2
    else:
        x = (num - 1) // 3
        y = (num - 1) % 3
    return (x,y)
    
def distance(now, goal):
    n_x, n_y = now
    g_x, g_y = goal
    return abs(n_x - g_x) + abs(n_y - g_y)

def solution(numbers, hand):
    # 좌표점이 필요함. 
    hand = "L" if hand == "left" else "R"
    hand_list = []
    l, r = "*", "#"
    for num in numbers:
        if num in {1,4,7}:
            hand_list.append("L")
            l = num
        elif num in {1,4,7}:
            hand_list.append("R")
            r = num
        else:
            n_point = find_point(num)
            l_point = find_point(l)
            r_point = find_point(r)
            l_distance = distance(l_point, n_point)
            r_distance = distance(r_point, n_point)
            if l_distance > r_distance:
                hand_list.append("L")
                l = num
            elif l_distance < r_distance:
                hand_list.append("R")
                r = num
            else:
                hand_list.append(hand)
                if hand == "L":
                    l = num
                else:
                    r = num
    return "".join(hand_list)
