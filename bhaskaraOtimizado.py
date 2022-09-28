import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input("Digite o A: "))
    b = float(input("Digite o B: "))
    c = float(input("Digit e o C: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    if delta(a, b, c) < 0:
        print("Esta equação não possui raízes reais.")
    else:
        x1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)

        if delta(a, b, c) == 0:
            print("A raíz da equação será:", x1)
        if delta(a, b, c) > 0:
            x2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
            print("As raízes reais da equação serão:", x1, "e", x2)
