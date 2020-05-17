from typing import List
import collections
from functools import reduce


def test_is_p():
    input = [16, 16, 32]
    hcf = find_hcf(input)
    assert 16 == hcf


def find_hcf(input):
    if 1 in input:
        return 1
    else:
        hcf = 1
        for i in range(2, input[0] + 1):
            if sum([x % i for x in input]) == 0:
                hcf = i

        return hcf


def find_primes(low, high):
    primes = []
    for i in range(low, high + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n):
    for j in range(2, n // 2 + 1):
        if n % j == 0:
            return False

    return True


def is_prime_pair(a, b):
    ab = a * 10 ** (len(str(b))) + b
    ba = b * 10 ** (len(str(a))) + a
    return True if is_prime(ab) and is_prime(ba) else False


def test_is_prime_pair():
    assert is_prime_pair(7, 109)



