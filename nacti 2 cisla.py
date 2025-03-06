a = float(input("Zadejte první číslo: "))
b = float(input("Zadejte druhé číslo: "))

součet = a + b
součin = a * b
rozdíl = a - b

if b != 0:
    podíl  = a / b
else:
    podíl = "Nelze dělit nulou"

print(f"Součet : {součet}")
print(f"Součin :  {součin}")
print(f"Rozdíl : {rozdíl}")
print(f"Podíl  : {podíl}")
