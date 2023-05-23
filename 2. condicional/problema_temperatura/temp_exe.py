temp = input("Você vai digitar a temperatura em qual escala (C/F)? ")

if temp == "F":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = 5/9*(f-32)
    print(f"Temperatura equivalente em Celsius: {c:.2f}")
elif temp == "C":
    c = float(input("Digite a temperatura em Celsius: "))
    f = (9*c + 160)/5
    print(f"Temperatura equivalente em Fahrenheit: {f:.2f}")