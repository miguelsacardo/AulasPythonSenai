#banco que avalia a elegibilidade de empréstimos com base na idade e remda mensal dos clientes
idade_cliente = int(input("Informe a sua idade: "))
renda_mensal = float(input("Informe sua renda mensal: "))

if idade_cliente >= 18 and renda_mensal > 1500.00:
    print(f"Você pode pedir um empréstimo! Você tem {idade_cliente} anos e {renda_mensal} de renda.")
elif idade_cliente < 18 and renda_mensal > 1000.00:
    print(f"Você pode pedir um empréstimo! Você tem {idade_cliente} anos e {renda_mensal} de renda.")
else:
    print("Você não pode obter empréstimo.")