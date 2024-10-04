#converter notas em letras
input_nota = float(input("Insira sua nota: "))

#converter nota
if input_nota > 10 or input_nota < 0:
    print(f"A nota é inválida. Nota informada: {input_nota}")
elif input_nota >= 9:
    print(f"Sua nota é A. Nota informada: {input_nota}")
elif input_nota >= 7 :
    print(f"Sua nota é B. Nota informada: {input_nota}")
elif input_nota >= 5 :
    print(f"Sua nota é C. Nota informada: {input_nota}")
elif input_nota >= 3 :
    print(f"Sua nota é D. Nota informada: {input_nota}")
elif input_nota >= 0 :
    print(f"Sua nota é E. Nota informada: {input_nota}")

