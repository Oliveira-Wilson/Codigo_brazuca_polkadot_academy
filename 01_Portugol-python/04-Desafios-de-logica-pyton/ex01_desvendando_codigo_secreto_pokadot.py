# Função para decifrar o código
def decifrar_codigo(inicio, fim):
    total = 0
    for numero in range(inicio, fim + 1):
        if numero % 3 == 0 and numero % 5 == 0:
            continue  # Ignorar múltiplos de 3 e 5
        elif numero % 3 == 0:
            total += numero  # Somar múltiplos de 3
        elif numero % 5 == 0:
            total -= numero  # Subtrair múltiplos de 5
    return total

# Entrada do usuário
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Cálculo e exibição do resultado
resultado = decifrar_codigo(inicio, fim)
print(f"O valor total calculado é: {resultado}")