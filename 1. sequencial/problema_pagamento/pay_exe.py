nome = input("Nome: ")
v = float(input("Valor por hora: "))
h = int(input("Horas trabalhadas: "))

pay = v * h

input(f"O pagamento para {nome} deve ser {pay:.2f}")