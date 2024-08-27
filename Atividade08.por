programa
{
  funcao inicio()
  {
    // Declara uma variável inteira para armazenar o ano
    inteiro ano

    // Solicita ao usuário para digitar um ano
    escreva("Digite um ano: ")

    // Lê o valor inserido pelo usuário e armazena na variável 'ano'
    leia(ano)

    // Verifica se o ano é bissexto usando a lógica correta
    se (ano % 4 == 0) // Divisível por 4
    {
      se (ano % 100 != 0) // Não divisível por 100
      {
        escreva("O ano é bissexto")
      }
      senao se (ano % 400 == 0) // Divisível por 400
      {
        escreva("O ano é bissexto")
      }
      senao
      {
        escreva("O ano não é bissexto")
      }
    }
    senao
    {
      escreva("O ano não é bissexto")
    }
  }
}