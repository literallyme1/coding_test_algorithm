
a = [1, 12, -5, -6, 50, 3]
k = 4
sum = sum(a[:4])
result = sum
left = 0
for right in range(4, len(a)):
    sum += a[right]
    sum -= a[left]
    left += 1
    result = max(result, sum)

print(result)


#7일차 