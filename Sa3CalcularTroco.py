# SESI SENAI Florianópolis-SC, Curso Técnico: Desenvolvimento de Sistemas (EAD)
# Unidade Curricular: 6.Programação de Aplicativos, Professor: Julio Cezar Rutke
# Situação de Aprendizagem: 3, Aluno: Bento Miguel Alves Martins
# Ultima Edição em: 05/07/2021 14:02

# Este algoritmo foi desenvolvido para otimizar a quantidade de unidades
# das notas e moedas que são retornadas no troco de uma compra, obtendo
# o valor da compra e o valor do pagamento.

valorCompra = float(input("Valor da Compra: R$"))
valorRecebido = float(input("Valor Recebido: R$"))

troco = float('{0:.2f}'.format(valorRecebido - valorCompra))

if troco <= 0:
    print("Troco Inexistente!")
else:
    print("Troco: R$", troco)

    # Função para otimizar unidades:
    def contarUnidades(valorTotal, valorUnidade):
        contador = 0

        while valorTotal >= valorUnidade:
            contador += 1
            valorTotal -= valorUnidade

        return valorTotal, contador


    valoresNotas = [200, 100, 50, 20, 10, 5, 2]
    valoresMoedas = [1, 0.50, 0.25, 0.10, 0.05]

    for i in range(len(valoresNotas)):
        troco, unidades = contarUnidades(troco, valoresNotas[i])

        if unidades > 0:
            print(unidades, "Nota(s): R$", valoresNotas[i])

    for i in range(len(valoresMoedas)):
        troco, unidades = contarUnidades(troco, valoresMoedas[i])

        if unidades > 0:
            print(unidades, "Moeda(s): R$", valoresMoedas[i])
