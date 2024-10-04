#determinar maior e menor idade entre três pessoas
idade_um = int(input("Digite a primeira idade: "))
idade_dois = int(input("Digite a segunda idade: "))
idade_tres = int(input("Digite a terceira idade: "))

#verificar maior e menor idade
if idade_um < idade_dois:
    maior_idade = idade_dois
    menor_idade = idade_um
else:
    maior_idade = idade_um
    menor_idade = idade_dois

#comparar idade 3
if idade_tres < maior_idade and idade_tres < menor_idade:
    menor_idade = idade_tres
elif idade_tres > maior_idade and idade_tres > menor_idade:
    maior_idade = idade_tres

print(f"maior idade {maior_idade} e menor idade {menor_idade}")