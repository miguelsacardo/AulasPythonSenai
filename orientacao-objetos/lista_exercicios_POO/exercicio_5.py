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
    def __init__(self, saldo):
        self.saldo = saldo
        self.historico_transacoes = []

    #método depositar - > adiciona o valor ao saldo e registra a transaçção no histórico
    def deposisar(self, his_transacoes):
        self.saldo += his_transacoes
        self.historico_transacoes.append(his_transacoes)

        return self.saldo
    
    #método sacar -> diminuir o valor do sado e registrar a transação (não permite saldo negativo)
    def sacar(self):
        pass

    #método extrato
    def extrato(self):
        for i in self.historico_transacoes:
            print("T", i)

#input usuário
depositar = float(input("Valor de depósito: "))

#instanciando classe
meu_banco = TransacaoBancaria(100)

print(f"Depósito: {meu_banco.deposisar(depositar)}")
print(f"Extrato: {meu_banco.extrato()}")