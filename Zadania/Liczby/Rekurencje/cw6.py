def nwd_iter(a,b):
    while b:
        a,b = b,a%b
    return a

def nwd_rek(a,b):
    if b == 0:
        return a
    return nwd_rek(b, a%b)

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print(nwd_iter(a,b))
print(nwd_rek(a,b))