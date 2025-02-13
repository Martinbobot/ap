max = 0
for i in range(10):
    print("Zadejte cislo")
    cislo = int(input())
    if cislo > max:
        max = cislo
print("nejvetsi zadane cislo bylo: " + str(max))
