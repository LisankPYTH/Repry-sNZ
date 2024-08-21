numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 0
primes_ = []
not_primes_ = []
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        continue
    else:
        f = n ** (1 / 2)
    for j in range(2, int(f + 1)):
        if n % j == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes_.append(n)
    else:
        primes_.append(n)
print("Primes:", primes_)
print("Not Primes:", not_primes_)
