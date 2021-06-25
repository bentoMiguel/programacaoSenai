valores = []

for i in range(20):
    valores.append(int(input("informe o próximo valor: ")))

print("Média:", sum(valores)/len(valores))
print("Maior:", max(valores))
print("Menor: ", min(valores))
