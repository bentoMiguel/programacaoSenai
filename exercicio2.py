valores = []
for i in range(4):
    valores.append(float(input("informe um número: ")))

total = 0
i = 0
while i < len(valores):
    total += valores[i]
    i += 1

media = total/len(valores)

if media > 1:
    print("Média maior que 1: \"positivo\"")
else:
    print("Média menor ou igual a 1: \"negativo\"")

print("A média é:", media)
