def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

while True:
    try:
        cislo = int(input("Zadejte číslo pro výpočet faktoriálu (větší nebo rovno nule): "))
        if cislo < 0:
            print("Prosím, zadejte číslo větší nebo rovno nule.")
        else:
            break
    except ValueError:
        print("To není platné číslo. Zkuste to znovu.")

vysledek = faktorial(cislo)
print(f"Faktoriál čísla {cislo} je {vysledek}.")
