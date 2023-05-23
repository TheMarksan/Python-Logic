code = int(input("Código do produto comprado: "))
q = int(input("Quantidade comprada: "))


def all_code(code):
    match code:
        case 1:
            v = q * 5.00
            return v
        case 2:
            v = q * 3.50
            return v
        case 3:
            v = q * 4.80
            return v
        case 4:
            v = q * 8.90
            return v
        case 5:
            v = q * 7.32
            return v


valor = all_code(code)

print(f"Valor a pagar: R$ {valor:.2f}")
