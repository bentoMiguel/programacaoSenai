valorCompra = float(input("Valor da Compra: R$"))
valorRecebido = float(input("Valor Recebido: R$"))

troco = valorRecebido - valorCompra

valoresNotas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]


def otimizar(valorTroco, valoresNotas):
    unidadesDeNotas = []

    for i in range(len(valoresNotas)):
        contador = 0

        while valorTroco >= valoresNotas[i]:
            contador += 1
            valorTroco -= valoresNotas[i]

        unidadesDeNotas.append(contador)

    return unidadesDeNotas


notasNecessarias = otimizar(troco, valoresNotas)

print("Troco: R$", troco)

for i in range(len(valoresNotas)):
    if notasNecessarias[i] != 0:

        if valoresNotas[i] > 1:
            print(notasNecessarias[i], "Nota(s): R$", valoresNotas[i])
        else:
            print(notasNecessarias[i], "Moedas(s): R$", valoresNotas[i])
