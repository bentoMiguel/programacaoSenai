valores = []
for i in range(4):
    valores.append(int(input("informe um número: ")))

total = 0
for i in range(len(valores)):
    total += valores[i]

media = total/len(valores)

if media > 1:
    print("positivo")
else:
    print("negativo")
