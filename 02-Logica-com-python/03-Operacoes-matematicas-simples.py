# Solicita o primeiro número ao usuário
numero1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número ao usuário
numero2 = float(input("Digite o segundo número: "))

# Realiza as operações matemáticas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
# Verifica se o divisor não é zero para evitar erro de divisão por zero
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Divisão por zero não é permitida"

# Exibe os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)