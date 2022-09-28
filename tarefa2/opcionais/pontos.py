import math

# coordenadas de um ponto em um plano cartesiano
x1 = int(input("Digite o x: "))
y1 = int(input("Digite o y: "))

# coordenadas de x e y de um outro ponto no mesmo plano cartesiano
x2 = int(input("Digite o x2: "))
y2 = int(input("Digite o y2: "))

# calcular a distância entre os dois pontos
distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if distance >= 10:
    print("longe")
else:
    print("perto")

