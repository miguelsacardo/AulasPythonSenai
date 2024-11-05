#nível 1 - sistema básico de controle financeiro

'''
    1 - registrar transação
        *o usuário escolhe entre registrar uma receita [1] ou uma despesa [2]
        *solicitar o valor e uma breve descrição para a transação
        *adicionar a transaação a uma lista, onde cada transação será um dicionário com as informações:
            "tipo" - especifica se é uma receita ou despesa
            "valor" - o valor da transação
            "descrição" - uma breve descrição para identificar a transação

        *ajuste o saldo total somando ou subtraindo o valor, dependendo do tipo de transação

    2 - Visualizar saldo atual
        *exibir o saldo atual, que considera todas as receitas e despesas registradas até o momento
        *criar função exibir_saldo que ao ser chamada imprime o saldo atual

    3 - Listar transações
    *exibir todas as transações até o momento, incluindo o tipo (receita ou despesa), valor e descrição
    *criar uma função listar_transações para exibir cada transação em uma linha, com informações formatadas

    4 - Sair
    *Finalizar o programa quando o usuário escolher a opção "Sair"

    criar funções para cada uma das funcionalidades principais:
        registrar_transacao
        exibir_saldo
        listar_transacoes

    o saldo deve ser iniciado como 0 e na medida que o usuário gera receitas, ele é incrementado. O saldo pode ficar negativo
    um while deve controlar a execução do programa até que o usuário selecione "Sair"
    o controle de fluxo pode ser com if/else ou com match case

    quando a opção "Registrar transação " é selecionada, verifique se o valor é positivo antes de adicionar ao saldo ou subtrair
    exiba mensagens de confirmação, como "Transação registrada" ou "saldo atualizado", após cada operação


'''

#registra transações (receitas e despesas)
#consultar o saldo atual e listar todas as transações registradas

#o usuário escolhe entre 2 opções
#ele deve informar um valor e uma descrição
#toda transação será um dicionário dentro de uma lista

#o saldo deve começar 0 e na medida que o usuário informa receitas, o saldo aumenta
#ao selecionar receitas, o valor da receita soma no saldo
#se o usuário informar espesas, o valor da despesa diminui no salário

#a função mostrar saldo atual deve calcular as receitas e despesas e mostrar sempre o resultado final

lista_transacao = []
transacoes = {}

class GerenciadorFinancas:
    def __init__(self,tipo,valor, descricao):
        self.saldo = 0
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao

    def registrarTransacoes(self):
        transacoes['Tipo'] = self.tipo
        transacoes['Valor'] = self.valor
        transacoes['Descricao'] = self.descricao

        lista_transacao.append(transacoes.copy())

        return lista_transacao

    def calcularSaldo(self):
        if self.tipo == "RECEITA":
            self.saldo = self.saldo + self.valor
        elif self.tipo == "DESPESA":
            self.saldo = self.saldo - self.valor

        return self.saldo

while True:

    # *o usuário escolhe entre registrar uma receita [1] ou uma despesa [2]
    escolhaUsuario = int(input("Escolha uma opção \n [1]Receita \n [2]Despesa \n [3]Sair \n"))

    match escolhaUsuario:
        case(1):
            print("Você escolheu registrar uma RECEITA")

            #solicitar os dados do usuário
            registroTipo = "RECEITA"
            registroValor = float(input("Informe o valor da sua receita: \n"))
            registroDesricao = str(input("Escreva a descrição do seu registro: \n"))

            print("\n", "-" * 50, "\n")

            print(f"Tipo de registro: {registroTipo} \n Valor: {registroValor} \n Descricao: {registroDesricao} \n")
            enviarEscolha = str(input("Você confirma o salvamento das informações acima? [S/N] \n")).upper()[0]

            if enviarEscolha == "S":
                gerenciamento_fincanceiro = GerenciadorFinancas(registroTipo, registroValor, registroDesricao)
                print(f"Registro da sua transação feita com sucesso!")

                print("\n", "-" * 50, "\n")

                #chama a função de registrar os dados
                gerenciamento_fincanceiro.registrarTransacoes()

                #chama a função de calcular o saldo
                print(gerenciamento_fincanceiro.calcularSaldo())

            else:
                print(f"Seu registro não foi feito.")

                print("\n", "-" * 50, "\n")

        case(2):
            print("Você escolheu registrar uma DESPESA")

            #solicitar dados ao usuário
            registroTipo = "DESPESA"
            registroValor = float(input("Informe o valor da sua despesa: \n"))
            registroDesricao = str(input("Escreva a descrição do seu registro: \n"))

            print("\n", "-" * 50, "\n")

            print(f"Tipo de registro: {registroTipo} \n Valor: {registroValor} \n Descricao: {registroDesricao} \n")
            enviarEscolha = str(input("Você confirma o salvamento das informações acima? [S/N] \n")).upper()[0]

            if enviarEscolha == "S":
                gerenciamento_fincanceiro = GerenciadorFinancas(registroTipo, registroValor, registroDesricao)
                print(f"Registro da sua transação feita com sucesso!")

                print("\n", "-" * 50, "\n")

                # chama a função de registrar os dados
                gerenciamento_fincanceiro.registrarTransacoes()

                # chama a função de calcular o saldo
                print(gerenciamento_fincanceiro.calcularSaldo())

            else:
                print(f"Seu registro não foi feito.")

                print("\n", "-" * 50, "\n")

        case(3):
            pass

# tipoT = str(input("Informe o tipo"))
# valorT = float(input("Informe  valor"))
# descricaoT = str(input("Digite uma descrição para a transição"))
# gerenciar = GerenciadorFinancas(tipoT, valorT, descricaoT)
#
#
# print(gerenciar.registrarTransacoes())



