# def é uma keyword usada pra definir funções, def = define (em inglês)
def soma(x, y, z):
    return x + y + z

def multiplica(x, y, z):
    return x * y * z

def nome_do_seu_time():
    return "Peñarol"

def quieta():
    x = 10 + 20
    print("O valor calculado é", x)

print(soma(10, 20, 30))
print(multiplica(20, 30, 100))
print(multiplica(soma(20, 40, 7), soma(65, 3, 2), multiplica(2, 3, 4)))
print(nome_do_seu_time())
quieta()