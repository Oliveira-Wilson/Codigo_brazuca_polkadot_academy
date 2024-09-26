# Inicializa variáveis para soma e contagem
soma = 0
contador = 0

while True:
    # Solicita ao usuário que insira uma nota
    nota = float(input("Digite uma nota (-1 para parar): "))
    
    # Verifica se o usuário deseja parar
    if nota == -1:
        break
    
    # Adiciona a nota à soma e incrementa o contador
    soma += nota
    contador += 1

# Verifica se foram inseridas notas
if contador > 0:
    media = soma / contador
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")