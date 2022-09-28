def fatorial(n):
    total = 1
    while (n > 0):
        total *= n
        n -= 1
    return total

def coeficiente_binomial(n, k):
    resultado = fatorial(n) / (fatorial(k) * fatorial(n - k))
    return resultado

