
# Verificar a existência da letra 'a' (maiúscula ou minúscula) em uma string e contar quantas vezes ocorre
def letraA(input_string):
    count = input_string.lower().count('a')
    return f"A letra 'a' aparece {count} vez(es) na string."

string_exemplo = "Amazônia é a maior floresta tropical do mundo."
resultado_contagem = letraA(string_exemplo)


print(letraA)
