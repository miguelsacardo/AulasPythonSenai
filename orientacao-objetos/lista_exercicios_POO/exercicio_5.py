'''
5. Classe TransacaoBancaria. Crie uma classe TransacaoBancaria 
com atributos saldo e historico_transacoes (uma lista vazia). 
Adicione métodos depositar(valor), sacar(valor) e extrato(). 
No método depositar, adicione o valor ao saldo e registre a transação em historico_transacoes. 
No método sacar, diminua o valor e registre a transação, garantindo que não permite saldo negativo. 
O método extrato() deve imprimir todas as transações e o saldo atual.'''

#criação da classe
class TransacaoBancaria:

    #atributos
    def __init__(self):
        self.saldo = 0
        self.historico_transacoes = []
    
    #método depositar - > adiciona o valor ao saldo e registra a transaçção no histórico
    def deposisar(self, his_transacoes):

        #faz o calculo do saldo
        self.saldo += his_transacoes

        #registra a transação no histórico
        self.historico_transacoes.append(his_transacoes)

        return self.saldo
    
    #método sacar -> diminuir o valor do sado e registrar a transação (não permite saldo negativo)
    def sacar(self, saque):

        #verifica se o saldo não vai ficar negativo
        if self.saldo == 0:
            return "Seu saldo ficará negativo. Operação bloqueada!"
        else:

            #faz o calculo e registra a transação no histórico
            self.saldo -= saque
            self.historico_transacoes.append(saque)

        return saque

    #método extrato
    def extrato(self):

        #imprime o histórico de transações 
        for i in self.historico_transacoes:
            print("Transações: ", i)
        
        #exibe o saldo final
        print(f"O seu saldo atual é: {self.saldo}")


#instanciar classe
meu_banco = TransacaoBancaria()

#operações do usuário
while True:
    #o que o usuário pode acessar do programa
    acessoUsuario = str(input("[D]Fazer deposito \n[S]Sacar\n[E]Ver extrato\n[F]Fechar programa\n")).upper()[0]

    match acessoUsuario:
        case "D":
            depositar = float(input("Que valor você deseja depositar?\n"))

            #armazenar o valor do return da função "depositar()"
            saldoPosDeposito = meu_banco.deposisar(depositar)
            print(f"Depósito feito: {depositar}")

            # #exibir o saldo
            # print(f"Seu saldo agora é: {saldoPosDeposito}")

            print('\n', "-"*100, "\n")

        case "S":
            sacar = float(input("Que valor você deseja sacar?\n"))

            #armazenar o valor do return da função "sacar()"
            saldoPosSaque = meu_banco.sacar(sacar)
            print(f"Saque feito: {saldoPosSaque}")

            print("\n", "-" * 100, "\n")

        case "E":

            #exibir extrato
            meu_banco.extrato()

            print("\n", "-" * 100, "\n")

        case "F":
            break

        case _:
            print("Informe uma opção válida!")

#erro 1 -> eu estava colocando a classe dentro do loop while, então ela estava sendo instanciada sempre
#que o programa rodava. ELa deve persistir no programa e não inicializar várias vezes
#assim, o valor do saldo é incrementado corretamente

#erro 2 -> o extrato também não estava sendo incrementado pois eu instanciei o objeto várias vezes
#após colocar a instancia fora do loop, o programa começou a pegar normalmente