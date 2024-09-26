frutas = ['maçã', 'banana', 'laranja']
while True:
    item = input('Adicionar item à lista (ou digite "sair" para encerrar): ')
    if item.lower() == 'sair':
        break
    frutas.append(item)

print('Lista completa:')
for fruta in frutas:
    print('fruta:', fruta)
