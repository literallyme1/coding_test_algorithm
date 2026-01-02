# [State] 
# [Input] 6개면 주사위 (2 ≤ dice의 갯수 = n ≤ 10),1 ≤ dice[i]의 원소 ≤ 100 ,  2차원 정수 배열 dice
# [Logic]
#1. A가 먼저 n / 2개의 주사위 ->  B가 남은 n / 2
#2. 주사위 -> 나온 수들을 모두 합해 점수를 계산
#3. 점수가 더 큰 쪽이 승리하며, 점수가 같다면 무승부
#4. 가장 이길 확률이 많은 주사위 

#주사위 묶음 중에 n//2  배분 
# for a_idx in combinations(range(n), n // 2):

# 경우의 수 list 
# a_sum = [ sum(i) for i in product(*a_dices)]
# b 정렬
# for i in a_sum:
    #wins += bisect_left(b_sums, score) 내 점수(score)보다 작은 값의 개수를 반환

# [Output] 가 골라야 하는 주사위 번호를 오름차순으로 1차원 정수 배열
#win update, 관련 번호도 업데이트, max_win return, 주사위 번호+1

from itertools import product, combinations
from bisect import bisect_left

def solution(dices):
    n = len(dices)
    dices_index = [ i for i in range(n)]
    max_wins = 0
    wins_dice_index = []
    for indexs in combinations(dices_index, n//2):
        #1. A가 먼저 n / 2개의 주사위 ->  B가 남은 n / 2
        a_dices = [dices[i] for i in indexs]

        b_dices = [i for i in dices if  i not in a_dices] # 저 인덱스를 제외하고 어떻게 하지 
        a_sums = [sum(a) for a in product(*a_dices)] # 하나씩 뽑아주나봄. (* 까먹음)
        b_sums = [sum(a) for a in product(*b_dices)]
        b_sums.sort()

        wins = 0
        for i in a_sums: 
            wins += bisect_left(b_sums, i)
        if wins > max_wins:
            max_wins = wins
            wins_dice_index = list(indexs)

    return [index + 1 for index in wins_dice_index]


        



print(solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]))