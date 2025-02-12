import sys 

def sieve_of_eratosthenes(MAX):
    is_prime = [True] * (MAX + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(MAX ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i , MAX+1, i):
                is_prime[j] = False
    return is_prime

MAX = 1000000
prime_lists = sieve_of_eratosthenes(MAX)

input = sys.stdin.read
data = map(int, input().split())

for n in data:
    if n == 0:
        break

    found = False
    for a in range(3, n //2 + 1, 2): #1,2 -> 홀수 소수 X
        b = n - a

        if prime_lists[a] and prime_lists[b]:
            print(f"{n} = {a} + {b}")
            found = True
            break

    if not found:
        print("Goldbach's conjecture is wrong.")