import math

# constantes da equação de 2° grau
# ax² + bx + c = 0
a = float(input("Digite o A: "))
b = float(input("Digite o B: "))
c = float(input("Digite o C: "))

# usar fórmula de bhaskara, imprimir as raízes
delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)

    if delta == 0:
        print("a raiz desta equação é", x1)
    if delta > 0:
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        if x1 < x2:
           print("as raízes da equação são", x1, "e", x2)
        else:
           print("as raízes da equação são", x2, "e", x1)

