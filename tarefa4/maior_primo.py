# Números primos são aqueles divisíveis apenas por 1 e por eles mesmos.
def ehPrimo(k):
    i = 1
    prim = 0
    while (i <= k):
        if (k % i == 0):
            prim = i
        else:
            print("Não eh primo: ", i)
        i += 1
    return prim


ehPrimo(100)


# ehPrimo(2)