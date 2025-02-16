#백준 1107번 
# URL : https://www.acmicpc.net/problem/1107
#PyPy3 Code

def min_press(N, broken_buttons):
    min_count = abs(N - 100) # +1, -1 만 사용했을 때 눌러야 하는 버튼

    for num in range(1000000):
        str_num = str(num)
        for ch in str_num: #각 자릿수가 있는 지 
            if int(ch) in broken_buttons:
                break
        else: #else 가 잘 실행됐다면
            min_count = min(min_count, len(str_num) + abs(num - N))
        
    return min_count

N = int(input().strip()) #목표 채널
M = int(input().strip()) #고장난 버튼 개수
broken_buttons = set(map(int, input().split())) if M else set()

print(min_press(N, broken_buttons))