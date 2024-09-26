numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Inicializa a variável fatorial
fatorial = 1

# Verifica se o número é negativo
if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    # Loop para calcular o fatorial
    for i in range(1, numero + 1):
        fatorial *= i

    # Exibe o resultado
    print(f"O fatorial de {numero} é: {fatorial}")