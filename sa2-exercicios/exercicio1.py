array = [5, 7, 2, 9, 4, 1, 3]
print("lista = ", array, "\n")

print("tamanho;", end=" ")
tamanho = 0
i = 0

while i < len(array):
    tamanho += 1
    i += 1

print(tamanho)

print("maior valor;", end=" ")
maiorValor = -999999

for i in range(len(array)):
    if array[i] > maiorValor:
        maiorValor = array[i]

print(maiorValor)

print("menor valor;", end=" ")
menorValor = 999999

for i in range(len(array)):
    if array[i] < menorValor:
        menorValor = array[i]

print(menorValor)

print("soma de todos os elementos;", end=" ")
somaTotal = 0
i = 0

while i < len(array):
    somaTotal += array[i]
    i += 1

print(somaTotal)

print("ordem crescente;", end="  ")
for i in range(len(array)):
    for j in range(len(array)):
        if array[i] < array[j]:
            tempVar = array[i]
            array[i] = array[j]
            array[j] = tempVar

print(array)

print("ordem decrescente;", end="  ")
for i in range(len(array)):
    for j in range(len(array)):
        if array[i] > array[j]:
            tempVar = array[i]
            array[i] = array[j]
            array[j] = tempVar

print(array)
