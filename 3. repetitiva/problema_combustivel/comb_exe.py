code = int(input("Informe um código (1, 2, 3) ou 4 para pagar: "))

alcool = 0
gasolina = 0
diesel = 0

while code != 4:
    if code == 1:
        alcool = alcool + 1
    elif code == 2:
        gasolina = gasolina + 1
    elif code == 3:
        diesel = diesel + 1
    code = int(input("Informe um código (1, 2, 3) ou 4 para pagar: "))


print("MUITO OBRIGADO")
print(f"Álcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")