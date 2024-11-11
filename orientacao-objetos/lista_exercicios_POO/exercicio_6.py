'''GerenciadorFinanceiro
Atributos: contas -> dicionário (chaves são IDs de conta e os valores são instâncias
de uma classe Conta)
Cada Conta deve possuir os atributos saldo, historico_transacoes e tipo_conta (poupança e corrente)

Métodos: criar_conta(id_conta, tipo_conta) -> cria uma nova instancia de Conta e adiciona no dicionário
de contas

depositar(id_conta, valor) -> realiza um depósito na conta especificada e registra a transação no histórico

sacar(id_conta, valor) - > realiza um saque, garantindo que o saldo não fique negativo. Registra a transação

transferir(id_origem, id_destino, valor) -> realiza uma transferência entre duas contas diferentes, 
garantindo que a conta de origem  tenha saldo suficiente. Registra a transação em ambas as contas

consultar_extrato(id_conta) -> imprime o histórico de transações e o saldo da conta especificada

calcular_juros(id_conta) -> adiciona juros ao saldo se o tipo_conta for 'Poupança'.
Esse método simula juros simples e aumenta o saldo em uma porcentagem fixa.  
'''

#criação da classe
class GerenciadorFinanceiro:
    def __init__(self):

        #atributos da classe
        self.contas = {}

#Método que instancia a conta e adiciona no dicionário de contas
    def criar_conta(self, id_conta, tipo_conta):

        #instanciando a classe Conta
        nova_conta = Conta(tipo_conta)

        #adiciona no dicionário de contas o ID e a instância da classe Conta
        self.contas[id_conta] = nova_conta

        return self.contas
    
#Método que deposita dinheiro na conta especificada e registra a transação
    def depositar(self, id_conta, valorDeposito):

        #encontra o ID da conta do usuário
        for ids in self.contas.items():
            if id_conta == ids[0]:

                #faz o acrescimo no saldo
                ids[1].saldo += valorDeposito
                print("Seu depósito foi feito com sucesso!")
                # print(ids[1].tipo_conta)

                #registra transação no histórico
                ids[1].historico_transacoes.append(valorDeposito)

                #printa testesn(para ver se está funcionando)
                print(f"Seu histórico atual é: {ids[1].historico_transacoes}")
                print("O tipo da sua conta é: ",ids[1].tipo_conta)
                print(f"Seu saldo é {ids[1].saldo}")

#Método que saca dinheiro na conta especificada e registra a transação
    def sacar(self, id_conta, valorSaque):

        #encontra o ID da conta do usuário
        for ids in self.contas.items():
            if id_conta == ids[0]:

                if ids[1].saldo == 0:
                    print("Operação bloqueada! Seu saldo é zero e ficará negativo!")
                elif valorSaque > ids[1].saldo:
                    print("Operação bloqueada! Valor de saque é maior que seu saldo!")
                else:
                    #faz o decréscimo no saldo
                    ids[1].saldo -= valorSaque
                    print("Seu saque foi feito com sucesso!")

                    #registra a transação no histórico
                    ids[1].historico_transacoes.append(valorSaque)

                    #printa testes (para ver se está funcionando)
                    print(f"Seu histórico atual é: {ids[1].historico_transacoes}")
                    print("O tipo da sua conta é: ",ids[1].tipo_conta)
                    print(f"Seu saldo é {ids[1].saldo}")

#Método que transfere o dinheiro entre duas contas, garantindo que a conta de origem tenha saldo suficente
#ele registra a transação em ambas as contas
    def transferir(self, id_origem, id_destino, valorTransferencia):

        #encontra o ID de origem
        for ids in self.contas.items():
            if id_origem == ids[0]:

                #verifica se o saldo não é zero
                if ids[1].saldo == 0:
                    print("Não é possível realizar a transfêrencia pois seu saldo é zero!")
                elif valorTransferencia > ids[1].saldo:
                    print("Você não possui essa quantia para fazer transferência!")
                elif id_destino not in self.contas:
                    print("Informe um ID de destino que exista!")
                else:
                    #o valor de transferencia deve fazer um decrescimo do saldo de origem
                    ids[1].saldo -= valorTransferencia

                    #registra essa transação no histórico
                    ids[1].historico_transacoes.append(valorTransferencia)

                    print(f"Conta origem: {ids[0]}")
                    print(f"Saldo atual origem {ids[1].saldo}")

                    #encontra o ID de destino
                    for idsDestino in self.contas.items():
                        if id_destino == idsDestino[0]:

                            #recebe a transferência
                            idsDestino[1].saldo += valorTransferencia

                            #registra o recebimento no histórico
                            idsDestino[1].historico_transacoes.append(valorTransferencia)

                            #print testes
                            print(f"Conta destino: {idsDestino[0]}")
                            print(f"Saldo destino {idsDestino[1].saldo}")

#Método que consulta extrato -> mostra o histórico e saldo atual
    def consultar_extrato(self, id_conta):

        #encontra o ID da conta
        for ids in self.contas.items():
            if id_conta == ids[0]:
                #mostra o histórico
                print(f"Histórico de transações: {ids[1].historico_transacoes}")

                #mostra o saldo atual
                print(f"Saldo atual: R${ids[1].saldo}")

#método que calcula juros simples fixo de uma conta que seja do tipo "poupança"
    def calcular_juros(self, id_conta):

        #procura a conta
        for ids in self.contas.items():
            if id_conta == ids[0]:

                #verifica se o tipoConta é "poupança"
                if ids[1].tipo_conta == "Poupança":
                    #calculo de juros simples -> usando 0,44% ao mês
                    jurosSimples = ids[1].saldo * 0.0044 * 12
                    ids[1].saldo += jurosSimples

                    #retorna os juros
                    return round(ids[1].saldo, 2)
                else:
                    #caso a conta não for poupança
                    print("A conta deve ser poupança para ser feito o calculo de Juros!")

#criação da classe Conta
class Conta:
    def __init__(self, tipoConta):
        
        #atributos da classe herdada de GerenciadorFinanceiro
        self.saldo = 0
        self.historico_transacoes = []
        self.tipo_conta = tipoConta

#instanciando a classe
gerenciador_financeiro = GerenciadorFinanceiro()

#programa que o usuário irá utilizar
while True:

    #acesso do usuário
    acessoUsuario = int(input("Escolha uma opção\n[1]Criar conta\n[2]Depósito\n[3]Sacar\n[4]Transferência\n[5]Consultar Extrato\n[6]Calcular Juros Simples\n[7]Sair\nOpção: "))

    match acessoUsuario:
        case 1:
            print("\n", "="*100, "\n")

            idConta = int(input("Informe um ID para sua conta: "))
            tipoConta = str(input("Informe o tipo da sua conta [P]Poupança | [C]Corrente\n")).upper()[0]

            #faz a verificação do tipo de conta do usuário
            if tipoConta == "P":
                tipoConta = "Poupança"
                contaUsuario = gerenciador_financeiro.criar_conta(idConta, tipoConta)
            elif tipoConta == "C":
                tipoConta = "Corrente"
                contaUsuario = gerenciador_financeiro.criar_conta(idConta, tipoConta)
            else:
                print("Informe um tipo válido de conta.")
            
            #print de teste
            print(contaUsuario)

            print("\n", "="*100, "\n")

        case 2:
            print("\n", "="*100, "\n")

            #id do usuário
            idUsuario = int(input("Informe o ID da sua conta: "))

            #valor do depósito
            valorDeposito = float(input("Informe o valor que você deseja depositar: "))
            gerenciador_financeiro.depositar(idUsuario, valorDeposito)

            print("\n", "="*100, "\n")

        case 3:
            print("\n", "="*100, "\n")

            #id do usuário
            idUsuario = int(input("Informe o ID da sua conta: "))

            #valor do saque
            valorSaque = float(input("Informe o valor que você deseja sacar: "))
            gerenciador_financeiro.sacar(idUsuario, valorSaque)

            print("\n", "="*100, "\n")
            
        case 4:
            print("\n", "="*100, "\n")

            #id origem
            idOrigem = int(input("Informe o ID da sua conta: "))

            #id destino
            idDestino = int(input("Informe o ID da conta que receberá a transação: "))

            #valor da transferência
            valorTransferencia = float(input("Informe o valor que você deseja transferir: "))
            gerenciador_financeiro.transferir(idOrigem, idDestino, valorTransferencia)

            print("\n", "="*100, "\n")

        case 5:
            print("\n", "="*100, "\n")
            
            #id da conta
            idConta = int(input("Informe o ID da sua conta: "))

            #mostrar extrato
            gerenciador_financeiro.consultar_extrato(idConta)

            print("\n", "="*100, "\n")

        case 6:
            print("\n", "="*100, "\n")

            #id da conta
            idConta = int(input("Informe o ID da sua conta POUPANÇA para ter os juros aplicados: "))

            rendimento = gerenciador_financeiro.calcular_juros(idConta)

            if rendimento == None:
                print("Seu Juros não foi calculado.")
            else:
                #calculo de juros
                print(f"Ao longo de 12 meses, com uma taxa de 0,44% de juros ao mês, seu saldo agora é: R${rendimento}")

            print("\n", "="*100, "\n")

        case 7:
            break
        case _:
            print("\n", "="*100, "\n")
            print("Informe uma opção válida!")
            print("\n", "="*100, "\n")


#o segredo para a realização deste exercicio está no fato de que a instancia de conta é jogada como valor
#para cada ID no dicionário, ficando por exemplo 1: Objeto Conta
#assim, cada ID tem seu proprio objeto conta e conseguimos acessar seus atributos únicos para cada ID.

#melhorias -> percebe-se que nas funções, muitas delas devem procurar a conta com base no id. Então poderia pensar
#em colocar essa busca de conta em uma função e chamá-la quano necessário, fazerndo assim a reutilização do 
#código.