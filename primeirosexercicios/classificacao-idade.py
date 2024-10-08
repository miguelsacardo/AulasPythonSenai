#tabela de classificaçãp de idade
idade = int(input("Digite sua idade: "))

if idade >= 60:
    print(f"Você é idoso. Você tem {idade} anos.")
elif idade < 60 and idade >= 18:
    print(f"Você é adulto. Você tem {idade} anos.")
elif idade < 18 and idade >= 13:
    print(f"Você é adolescente. Você tem {idade} anos.")
elif idade < 13 and idade >= 2:
    print(f"Você é criança. Você tem {idade} anos.")
else:
    print(f"Você é um bebê. Você tem {idade} ano.")