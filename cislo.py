max = input("Zadejte cislo ")
for i in range(9):
    cislo = input("Zadejte cislo ")
    if cislo > max:
        max = cislo
print("Nejvetsi cislo bylo " + str(max))
