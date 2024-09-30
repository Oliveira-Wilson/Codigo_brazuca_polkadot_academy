def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def find_magic_number(start, end):
    for num in range(start, end + 1):
        if num % 4 == 0 and is_prime(num) and sum_of_digits(num) % 2 != 0:
            return num
    return None

# Entrada do usuário
start = int(input("Digite o início do intervalo: "))
end = int(input("Digite o fim do intervalo: "))

# Cálculo do número mágico
magic_number = find_magic_number(start, end)

# Saída do resultado
if magic_number:
    print(f"O 'Número Mágico' encontrado é: {magic_number}")
else:
    print("O 'Número Mágico' não foi encontrado.")
    