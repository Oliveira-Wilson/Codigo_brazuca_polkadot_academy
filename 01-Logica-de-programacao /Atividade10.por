programa
{
    funcao inicio()
    {
        // Declara vari�veis para armazenar o n�mero digitado e a contagem de positivos
        inteiro numero, contador = 0

        // Repete 5 vezes para ler 5 n�meros
        para(inteiro i = 1; i <= 5; i++)
        {
            // Solicita ao usu�rio que digite um n�mero
            escreva("Digite o n�mero ", i, ": ")
            leia(numero)

            // Verifica se o n�mero � positivo e incrementa o contador
            se (numero > 0)
            {
                contador++
            }
        }

        // Imprime o resultado final
        escreva("Voc� digitou ", contador, " n�meros positivos.")
    }
}