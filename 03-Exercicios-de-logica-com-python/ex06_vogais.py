# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ").upper()

# Inicializa um dicionário para contar as vogais
vogais = 'AEIOU'
contagem = {vogal: 0 for vogal in vogais}

# Loop para contar as vogais
for letra in frase:
    if letra in contagem:
        contagem[letra] += 1

# Exibe o resultado
print("Contagem das vogais:")
for vogal, quantidade in contagem.items():
    print(f"A vogal '{vogal}' aparece {quantidade} vezes.")