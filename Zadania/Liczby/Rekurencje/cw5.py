def iter(n):
    q = 0.25
    a1 = -128
    for i in range(1, n):
        a1 *= q
    return a1

def rek(n):
    if n == 1:
        return -128
    return rek(n - 1) * 0.25

n = int(input("Podaj n: "))
print(iter(n))
print(rek(n))
