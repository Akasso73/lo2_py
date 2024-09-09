def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def nwd_rec(a, b):
    if a == b:
        return a
    elif a > b:
        return nwd_rec(a - b, b)
    else:
        return nwd_rec(a, b - a)
    
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print(nwd(a, b))
print(nwd_rec(a, b))
