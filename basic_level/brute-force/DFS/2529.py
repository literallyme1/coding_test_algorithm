#순열 

k = int(input()) #부등호 개수
signs = input().split()#부등호 입력 

#최대값, 최소값 변수 초기화 
max_val = ""
min_val = ""

#방문 여부 체크 
visited = [False] * 10

def possible(x, y, sign):
    
    if sign == '<':
        return x < y
    elif sign == '>':
        return x > y
    return False
#현재 선택한 숫자의 위치 idx 
def backtrack(idx, num):
    global max_val, min_val

    if idx == k + 1:
        if not min_val:
            min_val = num
        else:
            max_val = num 
        return
    
    for i in range(10):
        if not visited[i]: 
            if idx == 0 or possible(int(num[-1]), i, signs[idx - 1]):
                visited[i] = True
                backtrack(idx + 1, num + str(i))
                visited[i] = False

# 백트래킹 시작
backtrack(0, "")

print(max_val)  # 최대값 출력
print(min_val)  # 최소값 출력