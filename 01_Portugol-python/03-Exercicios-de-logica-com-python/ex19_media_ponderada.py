nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# pesos
peso1 = 2
peso2 = 3
peso3 = 5

# média ponderada
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# resultado
print(f"A média ponderada é: {media_ponderada:.2f}")