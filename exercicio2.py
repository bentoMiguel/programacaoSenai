valores = []
media = 0

for i in range(4):
    valores.append(int(input("informe um número: ")))

media = sum(valores)/len(valores)

if media > 1:
    print("positivo")
else:
    print("negativo")
