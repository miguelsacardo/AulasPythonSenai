#pergunta pro usuário até onde a sequencia de fibonacci vai
inputUsuario = int(input("Insira até qual termo a sequência de Fibonacci vai: "))

#valores iniciais dos digitos de fibonacci
fibonacciPrimeiro = 0
fibonacciSegundo = 1

for i in range(inputUsuario):

    #somar o n°1 = 0 e o n°2 = 1 da sequencia de fibonacci
    soma = fibonacciPrimeiro + fibonacciSegundo

    #o segundo número passa a ser o primeiro
    fibonacciSegundo = fibonacciPrimeiro
    fibonacciPrimeiro = soma #o primeiro número passa a ser o resultado da primeira soma

    soma = fibonacciPrimeiro + fibonacciSegundo #uma nova soma é feita, agora com os valores mudados

    #exibir pro usuário
    print(soma)
