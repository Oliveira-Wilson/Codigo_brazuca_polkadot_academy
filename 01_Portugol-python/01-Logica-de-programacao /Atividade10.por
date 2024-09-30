programa
{
    funcao inicio()
    {
        // Declara variáveis para armazenar o número digitado e a contagem de positivos
        inteiro numero, contador = 0

        // Repete 5 vezes para ler 5 números
        para(inteiro i = 1; i <= 5; i++)
        {
            // Solicita ao usuário que digite um número
            escreva("Digite o número ", i, ": ")
            leia(numero)

            // Verifica se o número é positivo e incrementa o contador
            se (numero > 0)
            {
                contador++
            }
        }

        // Imprime o resultado final
        escreva("Você digitou ", contador, " números positivos.")
    }
}