from collections import deque

# 헬퍼 함수: 두 집합 사이에서 짝(target)을 찾으면 제거하고 True 반환
def check_pair(group1, group2, target):
    for card in list(group1):  # set을 list로 바꿔서 순회 (중간에 삭제하려고)
        mate = target - card
        
        # 짝꿍이 존재하는가?
        if mate in group2:
            # 주의: group1과 group2가 같은 집합(hand, hand)일 경우, 
            # 서로 다른 카드여야 함 (card != mate)
            if (group1 is group2) and (card == mate): 
                continue 
                
            # 짝을 찾았으니 제거 (구매/사용)
            group1.remove(card)
            group2.remove(mate)
            return True  # 생존 성공!
            
    return False  # 짝 못 찾음

def solution(coin, cards):
    n = len(cards)
    target = n + 1
    
    hand = set(cards[:n//3])
    deck = deque(cards[n//3:])
    drawn = set()
    
    round = 1
    
    while len(deck) >= 2:
        # 1. 카드 2장 뽑아서 일단 '찜(drawn)' 해두기
        c1 = deck.popleft()
        c2 = deck.popleft()
        drawn.add(c1)
        drawn.add(c2)
        
        # 2. 생존 판정 (순서가 중요!)
        
        # [1순위] 공짜로 생존 (내 손패끼리)
        if check_pair(hand, hand, target):
            pass # 통과 (코인 0)
            
        # [2순위] 1코인 내고 생존 (내 손패 + 찜한 카드)
        elif coin >= 1 and check_pair(hand, drawn, target):
            coin -= 1 # 통과
            
        # [3순위] 2코인 내고 생존 (찜한 카드끼리)
        elif coin >= 2 and check_pair(drawn, drawn, target):
            coin -= 2 # 통과
            
        # [4순위] 다 없으면 사망
        else:
            break  # 게임 오버 (여기서 끝!)
            
        # 다음 라운드 생존
        round += 1
        
    return round