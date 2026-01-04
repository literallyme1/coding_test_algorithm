#[state]  list 
#[input]  동전 coin개(0 ≤ coin ≤ n),  카드 뭉치(뽑는카드 정해짐, 1차원 정수 배열, 0부터 시작, 중복 X)
#my_cards(type set) = cards[:(n/6)]
#trash_list = []

#[logic]
#2. 카드를 두 장 뽑기 (while cards == 0) leftPop
# for i in iterator(my_cards): if n - i in my_cards elif n - i in set(tras_list) -> coin - 1 
#round += 1

from collections import deque
def solution(coin, cards):
    n = len(cards)
    my_cards = set(cards[:n//3])
    left_cards = deque(cards[n/3:])
    temp_card = set()
    round = 0
    while len(left_cards) >=2:
        # 두장 뽑기 

        temp_card.add(left_cards.popleft()) #set 에서 append 는 뭐지? 
        temp_card.add(left_cards.popleft())

        #1. my cards 에 있는 경우 
        if card_checking(n, my_cards, my_cards): 
            round += 1
            continue

        elif coin >= 1 and card_checking(n, my_cards, temp_card):
            round += 1
            coin -= 1
            continue
        
        elif coin >= 2 and card_checking(n, temp_card, temp_card):
            round += 1
            coin -= 2
            continue
        else:
            break


    return round + 1

def card_checking(n, targets,  cards):
    for card in list(cards):
        if (n+1) - card in targets:
            cards.remove(card)
            targets.remove((n+1) - card)
            return True
    
    return False


coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
print(solution(coin, cards))