#verificar se uma hora é válida
input_hora = int(input("Insira uma hora: "))
input_minutos = int(input("Insira um minuto: "))
input_segundos = int(input("Insira um segundo: "))

#verificar os valores
if input_hora > 23 or input_hora < 0:
    print(f"Uma hora não pode ser maior que 24 e nem menor que 0.")
elif input_minutos > 59 or input_minutos < 0:
    print(f"O minuto não pode ultrapassar 59 e não pode ser menor que zero.")
elif input_segundos > 59 or input_segundos < 0:
    print(f"Os segundos não podem ultrapassar 59 e nem serem menores que zero.")
else:
    print(f"O horário informado foi: {input_hora}:{input_minutos:02d}:{input_segundos:02d}")