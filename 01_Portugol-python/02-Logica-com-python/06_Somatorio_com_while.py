soma = 0
numero = -1  

print('Vamos somar os números. Digite 0 para sair.')

while numero != 0:
    numero = int(input('Digite um número: '))
    soma += numero  
print(f'A soma dos números digitados é: {soma}')
