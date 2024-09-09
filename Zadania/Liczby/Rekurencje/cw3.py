def ciag_rekurencja(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return ciag_rekurencja(n - 1) - ciag_rekurencja(n - 2) + 3

n = int(input("Podaj n: "))
print(ciag_rekurencja(n))