#[state]
#[input] matching word
target = "AAAAE" 
vowel = ['A', 'E', 'I', 'O', 'U']
#[logic]

count = 0
ans = 0 
def dfs(word, target):
    global ans, count 
    if len(word) >  5:
        return 

    if word :
        count += 1
        if word == target:
            ans = count
            return 
    
    for i in range(5):
        dfs(word + vowel[i], target)



    for i in range(5):
        if not visited[i]:
            dfs(word + vowel[i], target, count + 1)

dfs("", target, 0)
#[output] 몇번 째 단어

#  'A', 'E', 'I', 'O', 'U'

