def collatz(n):
    kroky = 0
    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        kroky += 1
    print(n)
    print(f"Počet kroků: {kroky}")


start_number = int(input("Zadej číslo pro Collatzův problém: "))
collatz(start_number)

