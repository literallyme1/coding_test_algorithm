from collections import deque

def compare_cards(target, a, b, coin, coin_num):
    for i in a:
        if target - i in b  and  coin >= coin_num:
            print(i, target - i)
            a.remove(i)
            b.remove(target - i)
            return True
    return False

def solution(coin, cards):

    picked_list = []
    dis_num = len(cards) // 3
    first_cards = cards[:dis_num]
    last_cards = deque(cards[dis_num:])
    round = 0
    target = len(cards) + 1
    # 1. 두개씩 가져오기
    for i in range(len(last_cards) // 2):
        picked_list.append(last_cards.popleft())
        picked_list.append(last_cards.popleft())

    # 2. 내 카드 중 낼 수 있는 거 확인

        if compare_cards(target, first_cards, first_cards, coin, 0):
            print("my_card + my_card")
            round += 1
            continue
        # 3. 코인 1개 이상, 뽑은 것중(저번 것 포함) 같이 낼 수 있는 지 확인 
        elif compare_cards(target, first_cards, picked_list, coin, 1):
            print("my_card + picked_card")
            round += 1
            coin -= 1
            continue
        # 4. 코인 2개 이상, 뽑은 2개 낼 수 있는 지 확인 
        elif compare_cards(target, picked_list, picked_list, coin, 2):
            print("my_card + picked_card")
            round += 1
            coin -= 2
            continue
        else:
            break
    return round + 1


cards = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]
coin = 3
round = solution(coin, cards)
print(round)