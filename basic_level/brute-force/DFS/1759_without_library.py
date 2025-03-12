
L, C = map(int, input().split())
chars = sorted(input().split())

vowels = {'a', 'e', 'i', 'o', 'u'} #모음

def backtrack(path, idx):
    if len(path) == L:
        vowel_count = sum(1 for ch in path if ch in vowels)
        consonant_count = L - vowel_count

        #최소 1개의 모음, 2개의 자음 조건
        if vowel_count >= 1 and consonant_count >= 2:
            print(''.join(path))
        return
    
    for i in range(idx, C):
        path.append(chars[i])
        backtrack(path, i + 1)
        path.pop()

backtrack([], 0)        

