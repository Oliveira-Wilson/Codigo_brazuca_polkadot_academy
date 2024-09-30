# Inicializa uma lista para armazenar os números
numeros = []

# Permite que o usuário insira números
while True:
    entrada = input("Digite um número (ou 'sair' para finalizar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, insira um número válido.")

# Verifica se a lista não está vazia
if numeros:
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)
    
    # Exibe os resultados
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhum número foi inserido.")