d = int(input("Digite a duração em segundos: "))

hora = d//3600
resto = d%3600
min = resto//60
seg = resto%60

print(f"{hora}:{min}:{seg}")
