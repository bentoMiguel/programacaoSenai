# PARTE DE CIMA: /\

tamanhoParteCima = 4
espacosDoInicio = 4
espacosDoMeio = 0

for linha in range(tamanhoParteCima):
    print(" " * espacosDoInicio, "*", end="")

    if linha == 0:
        print("")
        espacosDoInicio -= 2
    else:
        print(" " * espacosDoMeio, "*")
        espacosDoInicio -= 1

    espacosDoMeio += 2


# PARTE DE BAIXO: |_|

tamanhoParteBaixo = 4
espacosDoInicio = 2
espacosDoMeio = 5

for linha in range(tamanhoParteBaixo):
    if linha == 0:
        print("***", " " * espacosDoMeio, "***", sep="")

    elif linha == tamanhoParteBaixo - 1:
        print(" " * espacosDoInicio, "*****")

    else:
        print(" " * espacosDoInicio, "*", " " * espacosDoMeio, "*", sep="")
