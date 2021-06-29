lista = [5, 7, 2, 9, 4, 1, 3]
print("lista = ", lista, "\n")

print("tamanho;", end=" ")
tamanho = 0

for i in range(len(lista)):
    tamanho += 1

print(tamanho)

print("maior valor;", end=" ")
maiorValor = -999999

for i in range(len(lista)):
    if lista[i] > maiorValor:
        maiorValor = lista[i]

print(maiorValor)

print("menor valor;", end=" ")
menorValor = 999999

for i in range(len(lista)):
    if lista[i] < menorValor:
        menorValor = lista[i]

print(menorValor)

print("soma de todos os elementos;", end=" ")
total = 0

for i in range(len(lista)):
    total += lista[i]

print(total)

print("ordem crescente;", end="  ")
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i] < lista[j]:
            tempVar = lista[i]
            lista[i] = lista[j]
            lista[j] = tempVar

print(lista)

print("ordem decrescente;", end="  ")
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i] > lista[j]:
            tempVar = lista[i]
            lista[i] = lista[j]
            lista[j] = tempVar

print(lista)
