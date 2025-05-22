myList=list(range(1,11))
print(myList)

position = 2
while position +1 < len(myList):
    myList[position], myList[position+1]=myList[position+1], myList[position]
    position += 1
    print(myList)