# Lógica das sequências
def completar_sequencias():
    sequencia_a = [1, 3, 5, 7, 9]  # números ímpares
    sequencia_b = [2, 4, 8, 16, 32, 64, 128]  # potências de 2
    sequencia_c = [0, 1, 4, 9, 16, 25, 36, 49]  # quadrados perfeitos
    sequencia_d = [4, 16, 36, 64, 100]  # quadrados perfeitos pares
    sequencia_e = [1, 1, 2, 3, 5, 8, 13]  # sequência de Fibonacci
    sequencia_f = [2, 10, 12, 16, 17, 18, 19, 20]  # números sem o dígito 5
    return sequencia_a, sequencia_b, sequencia_c, sequencia_d, sequencia_e, sequencia_f

sequencias_completas = completar_sequencias()
print(f"Sequências: {sequencias_completas}")
