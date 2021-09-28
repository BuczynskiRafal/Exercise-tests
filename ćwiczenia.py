def is_prime(n):

    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def calculate(index):
    lista = []
    n = 4
    while len(lista) < index:
        if n == 2:
            lista.append(n)
            n = n + 1
        if is_prime(n):
            lista.append(n)
            print(n)
            n = n+1
    print(lista[index-1])

calculate(6)