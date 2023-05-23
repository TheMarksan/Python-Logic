glicose = float(input("Digite a medida da glicose: "))

if glicose <= 100.0:
    print("Classificação: normal")
elif glicose > 100 and glicose <= 140:
    print("Classificão: elevado")
else:
    print("Classificação: diabetes")