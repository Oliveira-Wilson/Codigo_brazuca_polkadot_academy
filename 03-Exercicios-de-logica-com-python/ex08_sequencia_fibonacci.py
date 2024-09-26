def fibonacci(n):
    sequencia = []
    a, b = 0, 1  # Começa com 0 e 1
    
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b  # Atualiza os valores de a e b
    
    return sequencia

# Solicita ao usuário o número de termos
n = int(input("Digite o número de termos da sequência de Fibonacci que deseja: "))
if n <= 0:
    print("Por favor, insira um número positivo.")
else:
    resultado = fibonacci(n)
    print("Os primeiros", n, "números da sequência de Fibonacci são:", resultado)