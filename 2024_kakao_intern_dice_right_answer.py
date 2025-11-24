from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    max_wins = 0
    answer = []

    #1. dice 뽑기
    for a_indices in combinations(range(n), n // 2):

        #a가 선택한 주사위 외 저장 
        b_indices = [i for i in range(n) if i not in a_indices]

        a_dice = [dice[i] for i in a_indices]
        b_dice = [dice[i] for i in b_indices]

        # 2. 5번 돌려 나올 수 있는 모든 경우만큼 덧셈
        # *a_dice : unpacking ( 가장 큰 리스트 제거), product : 눈금을 하나씩 뽑아서 만들 수 있는 모든 조합
        a_sums = [sum(p) for p in product(*a_dice)]
        b_sums = [sum(p) for p in product(*b_dice)]


        # 3. 이분탐색을 위한 정렬 
        b_sums.sort()

        # 4. 고속 비교 
        wins = 0 
        for a_val in a_sums:
            #bisect_left (값보다 작은 개 몇개인 지 알려줌.)
            count = bisect_left(b_sums, a_val)
            wins += count

        # 5. 최대 승수 갱신 
        if wins > max_wins:
            max_wins = wins
            answer = list(a_indices)
        
        return sorted([x + 1 for x in answer])