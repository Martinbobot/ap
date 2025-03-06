while True:            #cyklus, ktery bude probihat
cislo = input("Zadejte cislo: ")
if cislo.lstrip("-").isdigit():
    max = int(cislo) 
    break 
else:
      print("Nezadali jste cislo.")

while input("Pro ukonceni zadejte pismeno K") != "K":
    cislo = input("Zadejte cislo")
   if cislo.lstrip("-"). isdigit():
        cislo = int(cislo)
    if max < cislo:
        max = cislo 

        print("Nejvetsi cislo bylo: " + max)
