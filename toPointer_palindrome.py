# 투포인터
def if_palindrome(s):
    a, l = 0, len(s) -1

    while  a < l:
        if not s[a].isalnum():
            a += 1
            continue
        if not s[l].isalnum():
            l -= 1
            continue
        if s[a].lower() != s[l].lower():
            return False
        a += 1
        l -= 1
    return True

## 대소문자, 영숫자
s = input().replace(" ", "")
print(str(if_palindrome(s)))




# numbers = [2, 7, 11, 15]
# target = 9

# def find_target(numbers, target):
#     left, right = 0, len(numbers) - 1

#     while left < right:
#         total = numbers[left] + numbers[right]

#         if total == target:
#             return numbers[left], numbers[right]   # 값 반환

#         elif total < target:
#             left += 1   # 합이 작으면 왼쪽 이동 (값 크게)
#         else:
#             right -= 1  # 합이 크면 오른쪽 이동 (값 작게)

#     return None  # 못 찾았을 때는 None 반환

# result = find_target(numbers, target)

# if result:
#     print(result)
# else:
#     print("can't find number")
