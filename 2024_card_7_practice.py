from collections import deque

def check_and_pay(deck1, deck2, target):
    for card in list(deck1): #set -> list 복사본
        partner = target - card
        if partner in deck2:
            deck1.remove(card)
            deck2.remove(partner)
            return True
    return False


def solution(coin, cards):
    n = len(cards)
    target = n + 1
    my_hand = set(cards[:n//3])
    pending = set() # 뽑았지만 내게 아닌 카드 리스트 
    deck = deque(cards[n//3:])
    turn = 1

    # 1. 두개씩 가져오기 (덱이 떨어질 때까지 진행)
    while len(deck) >= 2:
        card1 = deck.popleft()
        card2 = deck.popleft()
        pending.add(card1)
        pending.add(card2)
        
# 2. 우선순위대로 낼 수 있는지 확인 (Greedy)
        
        # CASE 1: 내 손패만으로 해결 (코인 0개)
        if check_and_pay(my_hand, my_hand, target):
            turn += 1
            continue
            
        # CASE 2: 내 손패 1장 + 후보군 1장 (코인 1개)
        # 코인이 있고 && 짝을 찾으면
        if coin >= 1 and check_and_pay(my_hand, pending, target):
            coin -= 1
            turn += 1
            continue
            
        # CASE 3: 후보군 2장 (코인 2개)
        if coin >= 2 and check_and_pay(pending, pending, target):
            coin -= 2
            turn += 1
            continue
    return turn


cards = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]
coin = 3
turn = solution(coin, cards)
print(turn)