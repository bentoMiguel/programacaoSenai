valores = []

for i in range(20):
    valores.append(int(input("informe o próximo valor: ")))

total = 0
for i in range(len(valores)):
    total += valores[i]

maiorValor = -999999
for i in range(len(valores)):
    if valores[i] > maiorValor:
        maiorValor = valores[i]

menorValor = 999999
for i in range(len(valores)):
    if valores[i] < menorValor:
        menorValor = valores[i]

print("Média:", total/len(valores))
print("Maior:", maiorValor)
print("Menor:", menorValor)
