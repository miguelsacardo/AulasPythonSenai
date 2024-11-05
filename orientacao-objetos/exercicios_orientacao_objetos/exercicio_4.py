#crie uma classe livro com atributos titulo e autor, e um metodo resumo() que imprime ambos

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def resumo(self):
        print(f"O título do livro é {self.titulo} e o autor é {self.autor}")

titulo_livro = str(input("Informe o título do livro: "))
autor_livro = str(input("Informe o autor do livro: "))
meu_livro = Livro(titulo_livro, autor_livro)
meu_livro.resumo()