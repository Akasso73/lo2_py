def rekurencja(n):
    if n==1:
        return -3
    return iteracja(n-1) + 5

def iteracja(n):
    wynik = -3
    for i in range(1, n):
        wynik += 5
    return wynik

n = int(input("Podaj n: "))
print(iteracja(n))
print(rekurencja(n))
