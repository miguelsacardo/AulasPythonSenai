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

'''
nível 2 - categorias para as transações

o usuário deve inserir uma categoria 
modificar a função de registro para incluir a categoria
Adicione uma função para listar todas as transações de uma categoria específica, solicitando que o usuário insira a categoria desejada.
'''

'''
nível 3 - Relatórios Mensais e Análise

*função para exibir o total gasto e recebido em cada categoria. -> percorre as transações e soma os valores para cada categoria
*
'''

#variáveis para o registro das transações
lista_transacao = []
transacoes = {}
novoSaldo = 0

#variáveis para o registro de relatórios
relatoriosLista = []
relatorios = {}

class GerenciadorFinancas:
    def __init__(self,saldo,tipo,valor, descricao, categoria):
        self.saldo = saldo
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria

    def registrarTransacoes(self):
        transacoes['Tipo'] = self.tipo
        transacoes['Valor'] = self.valor
        transacoes['Descricao'] = self.descricao
        transacoes['Categoria'] = self.categoria

        print(f"Seu saldo depois da função é {self.saldo}")
        lista_transacao.append(transacoes.copy())

        return lista_transacao

#*criar função exibir_saldo que ao ser chamada imprime o saldo atual
def exibir_saldo():
    return novoSaldo
        
#*criar uma função listar_transações para exibir cada transação em uma linha, com informações formatadas
def listar_transacoes():
    for transacao in lista_transacao:
        print (f"Tipo da transação: {transacao['Tipo']} | Valor da transação: R${transacao['Valor']} | Descrição da transação: {transacao['Descricao']} | Categoria da transação: {transacao['Categoria']}")

# função para listar todas as transações de uma categoria específica
def listar_categorias(categoria):
    for transacao in lista_transacao:
        if transacao['Categoria'] == categoria:
            print (f"Tipo da transação: {transacao['Tipo']} | Valor da transação: R${transacao['Valor']} | Descrição da transação: {transacao['Descricao']} | Categoria da transação: {transacao['Categoria']}")

#função para calcular o total gasto em cada categoria
def totalCategoria(escolherCategoria):
    valorTotalReceitas = 0
    valorTotalDespesas = 0
    for transacao in lista_transacao:
        if transacao['Categoria'] ==  escolherCategoria:
            if transacao['Tipo'] == "RECEITA":  
                valorTotalReceitas += transacao['Valor']
                
            else:
                valorTotalDespesas += transacao['Valor']
                
   
    print(f"O valor total da RECEITA da categoria {transacao['Categoria']} é {valorTotalReceitas}")
    print(f"O valor total da DESPESA da categoria {transacao['Categoria']} é {valorTotalDespesas}")

    print("\n", "-" * 50, "\n")

#relatório mensal
def relatorioMes(mes, saldo):
    relatorios['Mes'] = mes
    relatorios['Saldo'] = saldo
    relatoriosLista.append(relatorios.copy())

def mostrarRelatorioMes(escolherMes):
    for relatorio in relatoriosLista:
        if relatorio['Mes'] == escolherMes:
            mesRelatorio = relatorio['Mes']
            saldoReatorio = relatorio['Saldo']
        
    print(f"Mês do relatório: {mesRelatorio} | Saldo do mês: {saldoReatorio}")
    

while True:

    # *o usuário escolhe entre registrar uma receita [1] ou uma despesa [2]
    escolhaUsuario = int(input("Escolha uma opção \n [1]Receita \n [2]Despesa \n [3]Visualizar Saldo Atual \n [4]Verificar Transações \n [5]Filtrar Registros por Categoria \n [6]Relatório e análise Mensal ou por Categoria \n [7]Sair \n"))

    match escolhaUsuario:
        case(1):
            #verificando se o saldo está negativo
            if novoSaldo < 0:
                print("\n", "-" * 50, "\n")

                print("Seu saldo está negativo! A receita será usada para cobrir sua dívida!")
            
                print("\n", "-" * 50, "\n")

            print("Você escolheu registrar uma RECEITA")

            #solicitar os dados do usuário
            registroTipo = "RECEITA"
            registroValor = float(input("Informe o valor da sua receita: \n"))
            registroDesricao = str(input("Escreva a descrição do seu registro: \n"))
            registroCategoria = str(input("Escreva a categoria (onde você gerou sua receita?): \n")).upper()
            regitroMes = str(input("Em que mês foi registrado essa receita? (Digite em formato 00) \n"))

            print("\n", "-" * 50, "\n")

            print(f"Tipo de registro: {registroTipo} \n Valor: {registroValor} \n Descricao: {registroDesricao} \n Categoria: {registroCategoria} \n")
            enviarEscolha = str(input("Você confirma o salvamento das informações acima? [S/N] \n")).upper()[0]

            if enviarEscolha == "S":
                #o saldo do usuário é somado de acordo com as receitas
                novoSaldo += registroValor 

                #registra no relatório mensal
                relatorioMes(regitroMes, novoSaldo)

                #instancia a classe
                gerenciamento_fincanceiro = GerenciadorFinancas(novoSaldo, registroTipo, registroValor, registroDesricao, registroCategoria)
                print(f"Registro da sua transação feita com sucesso!")

                print("\n", "-" * 50, "\n")

                #chama a função de registrar os dados
                gerenciamento_fincanceiro.registrarTransacoes()

            else:
                print(f"Seu registro não foi feito.")

                print("\n", "-" * 50, "\n")

        case(2):
            #verificando se o saldo está negativo OU IGUAL A 0
            if novoSaldo == 0:
                print("\n", "-" * 50, "\n")

                print("Seu saldo irá ficar negativo!")

                print("\n", "-" * 50, "\n")

            elif novoSaldo < 0:
                print("\n", "-" * 50, "\n")

                print("Seu saldo está negativo! O valor de dívida será aumentado!")

                print("\n", "-" * 50, "\n")

            print("Você escolheu registrar uma DESPESA")

            #solicitar dados ao usuário
            registroTipo = "DESPESA"
            registroValor = float(input("Informe o valor da sua despesa: \n"))
            registroDesricao = str(input("Escreva a descrição do seu registro: \n"))
            registroCategoria = str(input("Escreva a categoria (onde você gerou sua receita?): ")).upper()
            regitroMes = str(input("Em que mês foi registrado essa despesa? (Digite em formato 00) \n"))

            print("\n", "-" * 50, "\n")

            print(f"Tipo de registro: {registroTipo} \n Valor: {registroValor} \n Descricao: {registroDesricao} \n Categoria: {registroCategoria} \n")
            enviarEscolha = str(input("Você confirma o salvamento das informações acima? [S/N] \n")).upper()[0]

            if enviarEscolha == "S":
                #o saldo do usuário é decrementado de acordo com as despesas
                novoSaldo -= registroValor
                
                #registra no relatório mensal
                relatorioMes(regitroMes, novoSaldo)

                gerenciamento_fincanceiro = GerenciadorFinancas(novoSaldo, registroTipo, registroValor, registroDesricao, registroCategoria)
                print(f"Registro da sua transação feita com sucesso!")

                print("\n", "-" * 50, "\n")

                # chama a função de registrar os dados
                gerenciamento_fincanceiro.registrarTransacoes()

            else:
                print(f"Seu registro não foi feito.")

                print("\n", "-" * 50, "\n")
        
        # 2 - Visualizar saldo atual
        case(3):
            print("\n", "-" * 50, "\n")

            print(f"Seu saldo atual é R${exibir_saldo()}")

            if novoSaldo < 0:
                print("\nVocê está devendo! Gere receitas para cobrir sua dívida!")

            print("\n", "-" * 50, "\n")
        
        #3 - Listar transações
        case(4):
            print("\n", "-" * 50, "\n")

            listar_transacoes()

            print("\n", "-" * 50, "\n")
        
        #o usuário deve inserir uma categoria
        case(5):
            print("\n", "-" * 50, "\n")

            filtrarCategoria = str(input("Pesquise uma categoria para filtrar as transações: ")).upper()
            listar_categorias(filtrarCategoria)
            
            print("\n", "-" * 50, "\n")
        
        #calcula totais por categoria e saldo mensal
        case(6):

            filtroEscolha = str(input("Filtrar por mês [M] ou filtrar por categoria [C]? \n")).upper()[0]

            if filtroEscolha == "C":
                print("\n", "-" * 50, "\n")
                escolherCategoria = str(input("Insira a categoria que você deseja calcular o total de todas as transações: \n")).upper()
                print("\n", "-" * 50, "\n")
                totalCategoria(escolherCategoria)
            elif filtroEscolha == "M":  
                print("\n", "-" * 50, "\n")
                escolherMes = str(input("Que mês você deseja consultar? \n")).upper()
                print(f"No mês {escolherMes} você obteve: \n")
                mostrarRelatorioMes(escolherMes)
                print("\n", "-" * 50, "\n")

        #sair do programa
        case(7):
            print("A execução do programa parou!")
            break

        #caso nenhuma das opções for selecionada
        case(_):
            print("Selecione uma opção válida!")
        




