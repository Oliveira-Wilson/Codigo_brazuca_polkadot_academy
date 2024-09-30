def verificar_palindromo(texto):
    # Remove espaços e transforma em minúsculas
    texto_limpo = ''.join(texto.split()).lower()
    # Inverte o texto
    texto_invertido = texto_limpo[::-1]
    # Compara o texto original com o texto invertido
    return texto_limpo == texto_invertido

# Solicita ao usuário uma palavra ou frase
entrada = input("Digite uma palavra ou frase: ")
if verificar_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")