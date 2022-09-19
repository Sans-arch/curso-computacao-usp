import math

# constantes da equação de 2° grau
# ax² + bx + c = 0
a = float(input("Digite o A: "))
b = float(input("Digite o B: "))
c = float(input("Digite o C: "))

# usar fórmula de bhaskara, imprimir as raízes
delta = b ** 2 - 4 * a * c

# se delta < 0, não tem raízes reais
if delta < 0:
    print("Esta equação não possui raízes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)

    # se delta == 0, tem 1 raíz real igual a tal
    if delta == 0:
        print("A raíz da equação será:", x1)
    # se delta > 0, tem 2 raízes reais iguais a tais
    if delta > 0:
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("As raízes reais da equação serão:", x1, "e", x2)
