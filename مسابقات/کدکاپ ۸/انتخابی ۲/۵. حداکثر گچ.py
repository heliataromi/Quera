def divisors(n):
    all_divisors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            all_divisors.append(i)
            all_divisors.append(n // i)
    all_divisors.sort(reverse=True)
    return set(all_divisors)


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


def sth(n):
    maximum = 0

    if n == 1:
        return 0
    if is_prime(n):
        return 1

    for divisor in divisors(n):
        cost = sth(divisor) + 1
        maximum = max(maximum, cost)
        if cost < maximum:
            break

    return maximum


n = int(input())
print(sth(n))
