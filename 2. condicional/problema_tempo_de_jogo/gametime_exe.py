hi = int(input("Hora inicial: "))
hf = int(input("Hora final: "))

if hi < hf:
    time = hf - hi
else:
    time = (24 - hi) + hf

print(f"O JOGO DUROU {time} HORA(S)")