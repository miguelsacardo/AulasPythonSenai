#if-else programa que verifica se a nota do aluno é boa, média ou exelente
nota_aluno = float(input("Insira sua nota: "))

if nota_aluno >= 9.0 and nota_aluno <= 10.0:
    print(f"A nota {nota_aluno} é exelente!")
elif nota_aluno >= 7.0 and nota_aluno < 9.0: #se uma condição e outra forem verdadeiras, ele executa o bloco
    print(f"A nota {nota_aluno} é boa!")
elif nota_aluno >= 5.0 and nota_aluno < 9.0:
    print(f"A nota {nota_aluno} é média.")
elif nota_aluno < 0 or nota_aluno > 10.0:
    print(f"A nota {nota_aluno} foi informada incorretamente.")
else:
    print(f"A nota {nota_aluno} é insulficiente.")