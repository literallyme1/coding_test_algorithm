#백준 2609번 
# URL : https://www.acmicpc.net/problem/2609
#python 3 Code

#최대공약수 메소드 (유클리드 호제법)
def gcd(a, b):
    while b !=0:
        a, b = b, a % b
    return a

#최소공배수 메소드
def lcm(a, b):
    return (a * b) // gcd(a, b)

#입력과 출력 
a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))