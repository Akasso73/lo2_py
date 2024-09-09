def iteracja(n):
    bin = ""
    while n > 0:
        bin = str(n % 2) + bin
        n = n // 2
    return bin

def rekurencja(n):
    if n == 0:
        return ""
    else:
        return rekurencja(n // 2) + str(n % 2)

n = int(input("Podaj liczbę dziesiętną: "))
print(rekurencja(n))
print(iteracja(n))