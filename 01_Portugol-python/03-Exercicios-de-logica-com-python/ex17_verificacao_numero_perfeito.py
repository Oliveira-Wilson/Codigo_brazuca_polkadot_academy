numero = int(input("Digite um número: "))

# Inicializa a soma dos divisores
soma_divisores = 0

# Encontra os divisores próprios do número
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

# Verifica se o número é perfeito
if soma_divisores == numero:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")