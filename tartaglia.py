def sobre(m, n):
    """Calcula m sobre n."""
    if m == 0 and n > 0:
        return 0
    if m >= 0 and n == 0:
        return 1
    return sobre(m - 1, n - 1) + sobre(m - 1, n)


def factorial(n):
    """Calcula el factorial de n."""
    res = 1
    while n >= 1:
        res *= n
        n -= 1
    return res


def sobre2(m, n):
    """Otra forma de calcular m sobre n."""
    return factorial(m) // (factorial(n) * factorial(m - n))


def triangulo(filas) -> None:
    """Dibuja el triángulo de Tartaglia o Pascal."""
    for m in range(filas):
        # print(' ' * 2 * (filas - m), end='')
        for n in range(m + 1):
            print(f"{sobre(m, n):3}", end=' ')
        print()
