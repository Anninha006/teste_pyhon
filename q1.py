# Verificar se um número pertence à sequência de Fibonacci
def fibonacci(número):
    a, b = 0, 1
    while a <= número:
        if a == número:
            return f"O número {número} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {número} NÃO pertence à sequência de Fibonacci."

numero_fibonacci = 21
resultado_fibonacci = fibonacci(numero_fibonacci)
print(fibonacci)
