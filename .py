import random

pocet_hodu = 0

while True:
    kostka1 = random.randint(1, 1000)
    kostka2 = random.randint(1, 1000)
    pocet_hodu += 1
    print(f"Hod {pocet_hodu}: Kostka 1 = {kostka1}, Kostka 2 = {kostka2}")
    if kostka1 == kostka2:
        print(f"Obě kostky jsou stejné! Počet hodů: {pocet_hodu}")
        break
