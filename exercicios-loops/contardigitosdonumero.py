#usuário informa um número
digitoString = str(input("Informe um número: "))

numeroDigitos = 0 #variável que vai somar o total do número de digitos

#confirmar se o número é positivo
if digitoString[0] == "-":
    print("Informe um número positivo.")
else:
    while numeroDigitos < len(digitoString):
        numeroDigitos += 1 #incrementa a variável "numeroDigitos" enquanto ela for menor que a length da string do número


#verifica a quantidade de digitos para exibir o plural ou singular corretamente ao usuário.
if numeroDigitos == 1:
    print(f"O número que você informou tem {numeroDigitos} digito.")
else:
    print(f"O número que você informou tem {numeroDigitos} digitos.")


