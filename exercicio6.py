def conversorHoraMin(horas):
    print(horas, "hora(s) representa(am)", horas*60, "minutos!")


print("===== CONVERSÃO: Horas --> Minutos =====")
print("aviso: uma hora e meia (1:30) é representada como 1.5 horas")

horas = float(input("\nInforme a hora: "))

conversorHoraMin(horas)
