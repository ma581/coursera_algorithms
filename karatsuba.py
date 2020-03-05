from math import ceil, floor

base = 10


def karatsuba(x, y):
    n = len(str(x))
    if x < 10:
        return x * y
    else:
        n_over_2 = ceil(n / 2)

        x_high = (floor(x / 10 ** n_over_2))
        x_low = (x % (10 ** n_over_2))

        y_high = int(floor(y / 10 ** n_over_2))
        y_low = int(y % (10 ** n_over_2))

        a = karatsuba(x_high, y_high)
        d = karatsuba(x_low, y_low)
        e = karatsuba((x_high + x_low), (y_high + y_low)) - a - d
        return int(a * (base ** (n_over_2 * 2)) + e * (base ** n_over_2) + d)


def karat(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = karat(b,d)
        z1 = karat((a+b),(c+d))
        z2 = karat(a,c)

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(x,y) - x*y)
print(karat(x,y) - x*y)
# print(x*y)