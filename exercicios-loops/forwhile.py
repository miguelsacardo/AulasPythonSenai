#declaração de variáveis
x = 0
y = 5

for i in range(3): 
    while y > 0:
        if x % 2 == 0:
            y -= 2
        else:
            y -= 1
        x += 1
    y = 5

#exibe ao usuário
print(x,y)