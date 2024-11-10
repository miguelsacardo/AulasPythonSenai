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
        self.listaContas = []

#Método que instancia a conta e adiciona no dicionário de contas
    def criar_conta(self, id_conta, tipo_conta):
        nova_conta = Conta(tipo_conta)

        #adiciona no dicionário de contas
        self.contas['ID'] = id_conta
        self.contas['TIPO'] = tipo_conta

        self.listaContas.append(self.contas.copy())
        return self.listaContas

#herança de classe -> a classe Conta herda de GerenciadorFinanceiro
class Conta(GerenciadorFinanceiro):
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
    acessoUsuario = int(input("Escolha uma opção\n[1]Criar conta\n"))

    match acessoUsuario:
        case 1:
            idConta = int(input("Informe um ID para sua conta: "))

            #gerenciador_financeiro.criar_conta(idConta,'Poupança')

            for ids in gerenciador_financeiro.listaContas:
                if ids['ID'] != idConta:
                    gerenciador_financeiro.criar_conta(idConta, "Poupança")
                    print(ids)
                else:
                    print("aaa")