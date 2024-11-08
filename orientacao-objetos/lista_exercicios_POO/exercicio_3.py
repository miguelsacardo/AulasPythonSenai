'''
3. Classe Animal. Crie uma classe Animal com atributos especie e som.
Adicione o método emitir_som() que imprime o som do animal.
'''

#criação da classe
class Animal:
    def __init__(self, especie, som):
        
        #atributos 
        self.especie = especie
        self.som = som

    #método que emite o som do animal
    def emitir_som(self):
        return self.som
    

#input do usuário
especieAnimal = str(input("Informe a espécie do animal: "))
somAnimal = str(input("Informe o som que o animal faz: "))

#instanciando a classe
meu_animal = Animal(especieAnimal, somAnimal)

somMeuAnimal = meu_animal.emitir_som()
#mostrando ao usuário 
print(f"A espécie do animal é: {meu_animal.especie}\nO som do animal é {somMeuAnimal}")