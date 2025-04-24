import random

win = 0
lose = 0

iterations = int(input("Zadejte počet opakování který chcete simulovat"))
for i in range(iterations):
    print(i)
    car = random.randint(1,3)
    playersChoice = random.randint(1,3)
    while True:
        montysChoice = random.randint(1,3)
        if montysChoice != car and montysChoice != playersChoice:
            break
    #print(car,playersChoice,montysChoice)
    playersOld = playersChoice
    while True:
        playersChoice = random.randint(1,3)
        if playersChoice != montysChoice and playersChoice != playersOld:
            break
    if playersChoice == car:
        win += 1
    else:
        lose += 1 
print(f"Hráč prohrál v {lose} případech a zvítězil v {win} případech \n to znamená, že zvítezil v {(win/iterations)*100:.2f} % případu a prohrál v {(lose/iterations)* 100:.2f}% případu.")
