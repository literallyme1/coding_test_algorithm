from collections import deque

def solution(coin, cards):
    n = len(cards)
    target = n + 1  # 두 카드의 합이 n+1이 되어야 함
    
    # 1. 초기 세팅
    hand = set(cards[:n//3])          # 처음에 가진 카드 1/3
    deck = deque(cards[n//3:])        # 뽑을 카드 뭉치 (큐)
    drawn = set()                     # 뽑았지만 아직 안 산 카드들 (후보지)
    
    round = 1
    
    # 2. 게임 진행 (덱에 카드가 남아있는 동안)
    while len(deck) >= 2:
        # 카드 2장 뽑기 (일단 후보지에 저장)
        c1 = deck.popleft()
        c2 = deck.popleft()
        drawn.add(c1)
        drawn.add(c2)
        
        # 3. 생존 판정 (그리디)
        # 코인 0개로 hand끼리 해결 가능한가?
        for i in hand : 
            if hand in target - i : 
                hand.pop(i)
                hand.pop(target - i)
                break
            elif coin >= 1 and drawn in target - i:
                coin -= 1
                break
            elif coin >= 2 and sum(drawn):
                coin -= 2
                break
            else :
                return
        
        # drawn 지우기 
        drawn.clear()

        # 다음 라운드 진행
        round += 1
        
    return round
