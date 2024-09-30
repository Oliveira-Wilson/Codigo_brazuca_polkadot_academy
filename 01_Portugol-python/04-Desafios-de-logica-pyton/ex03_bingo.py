import random

def gerar_cartela():
    return random.sample(range(1, 76), 5)

def bingo():
    cartela = gerar_cartela()
    numeros_sorteados = []
    total_sorteios = 0

    print(f"Sua cartela: {cartela}")

    while cartela:
        numero = random.randint(1, 75)
        total_sorteios += 1
        numeros_sorteados.append(numero)

        print(f"Número sorteado: {numero}")

        if numero in cartela:
            print(f"Número {numero} acertado!")
            cartela.remove(numero)

    print(f"Todos os números foram acertados em {total_sorteios} sorteios!")

# Iniciar o jogo
bingo()