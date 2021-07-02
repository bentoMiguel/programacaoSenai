# PARTE DE CIMA: /\

espacosDoInicio = 4
espacosDoMeio = 0

for linha in range(4):
    print(" " * espacosDoInicio, "*", end="")

    if linha == 0:
        print("")
        espacosDoInicio -= 2
    else:
        print(" " * espacosDoMeio, "*")
        espacosDoInicio -= 1

    espacosDoMeio += 2


# PARTE DE BAIXO: |_|

espacosDoInicio = 2
espacosDoMeio = 5

for linha in range(4):
    if linha == 0:
        print("***", " " * espacosDoMeio, "***", sep="")

    elif linha == 3:
        print(" " * espacosDoInicio, "*****")

    else:
        print(" " * espacosDoInicio, "*", " " * espacosDoMeio, "*", sep="")
