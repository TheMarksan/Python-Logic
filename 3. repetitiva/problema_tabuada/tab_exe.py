n = int(input("Deseja a tabuada para qual valor? "))

for i in range(1, 11):
    mult = n * i
    print(f"{n} x {i} = {mult}")