from itertools import combinations, product
from bisect import bisect_left
def solution(dice_list): 
    result = 0
    # choose_dice = 
    #1. 2/n 개씩 주사위를 배분한다.
    dice_num = len(dice_list)
        
    #2. 자기 주사위 중 2 숫자씩 뽑는 모든 경우의 수 배열
    for my_index in combinations(range(dice_num), dice_num//2):
        # 상대 리스트 
        win = 0
        your_index = [x for x in range(dice_num) if x not in my_index]
        my_list = [dice_list[x] for x in my_index]
        your_list = [dice_list[x] for x in your_index]
        my_sum = [sum(x) for x in product(*my_list)]
        your_sum = [sum(x) for x in product(*your_list)]

        #3. 이진탐색, 이길 수 있는 개수 합산 
        your_sum.sort()
        for target in my_sum:
            win += bisect_left(your_sum, target)
        # 이길 수 있는 확률 이 가장 높다면 
        if result < win : 
            result = win
            result_index = my_index
    return [x + 1 for x in result_index]

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
print(solution(dice))