#백준 1759번 
# URL : https://www.acmicpc.net/problem/1759
#PyPy3 Code

from itertools import combinations

# 입력 받기
L, C = map(int, input().split())
chars = sorted(input().split())

# 모음과 자음 정의
vowels = {'a', 'e', 'i', 'o', 'u'}

# 가능한 모든 조합 생성
for comb in combinations(chars, L):
    # 모음 개수, 자음 개수 세기
    vowel_count = sum(1 for ch in comb if ch in vowels)
    consonant_count = L - vowel_count
    
    # 조건: 최소 1개의 모음, 최소 2개의 자음
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(comb))