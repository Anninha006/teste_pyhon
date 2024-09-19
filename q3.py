# Valor da variável SOMA 
def calcular_soma():
    INDICE = 12
    SOMA = 0
    K = 1
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    return SOMA

valor_soma = calcular_soma()
print(f"Valor de SOMA: {valor_soma}")

