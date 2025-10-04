
## ------------------ 가변 크기 -------------------

s = "eceba"

left = 0
best = 0
cur_count = 0

for i, a in enumerate(s):
    if len(tuple(s[:i])) < 2:
        cur_count += i+1
        best = max(cur_count, best)
    else:
        for j in range(1, i-3):
            if len(tuple(s[j:i])) <= 2: 
                cur_count = len(tuple(s[j:i]))
                best = max(cur_count, best)
                break
print(best)    


    



# ## ------------------ 고정 크기 ------------------

# a = [1, 12, -5, -6, 50, 3]
# k = 4

# cur = sum( a[:4])
# best = cur 

# for i in range(4, len(a)):
#     cur += a[i]
#     cur -= a[i - k]

#     best  = max(cur, best)
    
# print(best)