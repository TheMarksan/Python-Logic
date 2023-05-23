n = int(input("Quantos casos você vai digitar? "))

for i in range(0, n):
    print("Digite três números: ")
    a = float(input())
    b = float(input())
    c = float(input())
    mediaP = (a*2+b*3+c*5)/10
    print(f"MÉDIA = {mediaP:.1f}")