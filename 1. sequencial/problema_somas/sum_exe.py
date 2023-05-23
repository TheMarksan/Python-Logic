
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de y: "))
op = input("Qual das 4 operações deseja realizar? (+/-/x/d): ")

def som(x, y):
    soma = x + y
    return soma
def sub(x, y):
    sub = x - y
    return sub
def mul(x, y):
    mul = x * y
    return mul
def div(x, y):
    div = x / y
    return div

if op == "+":
    result = som(x, y)
    print(f"Resultado = {result}")
elif op == "-":
    result = sub(x, y)
    print(f"Resultado = {result}")
elif op == "x":
    result = mul(x, y)
    print(f"Resultado = {result}")
elif op == "d":
    result = div(x, y)
    print(f"Resultado = {result}")



