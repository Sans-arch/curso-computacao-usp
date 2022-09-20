qtd_seq = int(input("Digite quantos numeros terá a sequência a ser somada: "))

soma = 0

while qtd_seq > 0:
    num = int(input("Digite um numero: "))
    soma = soma + num
    qtd_seq = qtd_seq - 1

print("A soma total dos numeros é:", soma)
