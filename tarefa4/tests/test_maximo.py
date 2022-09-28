def maximo(x, y):
    if(x > y):
        return x
    else:
        return y


# Testes automatizados
def test_maximo_2_3():
    assert maximo(2, 3) == 3

def test_maximo_negativo():
    assert maximo(-15, 40) == 40

def test_maximo_3_4():
    assert maximo(3, 4) == 4