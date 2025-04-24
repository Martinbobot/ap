myList = ["pomeranč", "jablko", "kumqat", "meloun", "švestka"]
print(myList)
print(len(myList))
print(myList[2])
#print(myList[int(input("Zadejte pozici"))])
dupList = myList[2:5]
print(myList)
print(dupList)

if "jablko" in myList:
    print("Jablko tam je")

myList[-2] = "Samice hrabáče"
print(myList)

myList.append("grep")
print(myList)