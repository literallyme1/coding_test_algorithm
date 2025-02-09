#백준 4375번 
# URL : https://www.acmicpc.net/problem/4375
#python 3 Code

def find_smallest_length(n):
    remainder = 1 # 1의 나머지 
    length = 1 # 1의 자릿수

    while remainder % n != 0: # 나누어지지 않으면
        remainder = (remainder * 10 + 1) % n #풀이과정 velog 확인
        length += 1
    
    return length

while True:
    try:
        n = int(input())
        print(find_smallest_length(n))
    except EOFError:
        break