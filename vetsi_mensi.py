print("Zadejte prvni cislo")
y = int(input())
print("zadejte druhe cislo")
x = int(input())
if x > y:
    print(str(x) + " je vetsi nez " + str(y))
elif x==y:
      print("čísla jsou stejná")
else:
        print(str(x) + " je mensi nez " + str(y))