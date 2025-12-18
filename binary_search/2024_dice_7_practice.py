## 최적 코드 
from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    # [핵심 1] 값 대신 '인덱스(0, 1...)'로 접근합니다.
    indices = range(n)
    
    max_wins = -1
    answer = []

    # A가 가져갈 주사위의 '인덱스 조합'을 뽑습니다.
    for a_indices in combinations(indices, n // 2):
        # [핵심 2] 차집합(set)을 이용해 상대방(B) 인덱스를 한방에 구합니다.
        # list comprehension으로도 가능하지만, set이 개념적으로 명확합니다.
        b_indices = [i for i in indices if i not in a_indices]
        
        # 인덱스로 실제 주사위 객체를 가져옵니다.
        a_dice = [dice[i] for i in a_indices]
        b_dice = [dice[i] for i in b_indices]
        
        # 주사위 눈금의 합 구하기 (product 활용 - 아주 잘하셨어요!)
        a_sums = [sum(x) for x in product(*a_dice)]
        b_sums = [sum(x) for x in product(*b_dice)]
        
        # [핵심 3] 이진 탐색(bisect)을 쓰려면 반드시 '정렬'해야 합니다.
        b_sums.sort()
        
        # 승수 계산
        wins = 0
        for score in a_sums:
            # bisect_left: 내 점수(score)보다 작은 값의 개수를 반환
            # 즉, 내가 이기는 경우의 수
            wins += bisect_left(b_sums, score)
            
        if wins > max_wins:
            max_wins = wins
            # 0-index를 1-index로 변환해서 저장
            answer = [x + 1 for x in a_indices]
            
    return answer
"""
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

"""



