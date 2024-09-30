from random import randint # rand int (randomiza um n inteiro)
from time import sleep     # O sleep faz o computador 'AGUARDAR um tempo/Pocessar/dormir'
computador = randint(0, 100) # faz o computador "PENSAR" 
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 100. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Digite um número de 0, a 100. ')) # JOGADOR tenta adivinhar

print('POCESSANDO...') 
sleep(3)

if jogador == computador: 
    print(f'Parabenś voce me  Venceu')
elif jogador < computador:
    print(f'Tente novamente,Voce perdeu!, o numero sorteado foi MENOR que o escolhido ')
elif jogador > computador:
    print(f'Tente novamente,Voce perdeu!, o numero sorteado foi MAIOR que o escolhido. ')