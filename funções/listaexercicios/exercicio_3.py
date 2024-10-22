'''3) Crie uma função chamada par_ou_impar() que recebe um número inteiro do usuário e retorna "Par" se o número for par, e "Ímpar" se for ímpar.'''

def par_ou_impar(numero):
     if numero % 2 == 0:
         return "Par."
     else:
         return "Ímpar."


numeroUsuario = int(input("Digite um número para saber se ele é par ou ímpar: "))
print(par_ou_impar(numeroUsuario))