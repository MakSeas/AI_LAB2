#Лаба 2




theList=[22,55,3,45,6,7,8,22,8,79,8,96,242]

print(f"Список: {theList}")

def Task1():
    plusResult=0
    multResult=1

    for number in theList:
        plusResult+=number
        multResult*=number

    print(f"Сумма элементов равна {plusResult}")
    print(f"Произведение элементов равно {multResult}")

def Task2():
    maxValue=theList[0]

    for number in theList:
        if number>maxValue:
            maxValue=number

    print(f"Максимальное число списка равно: {maxValue}")

def Task3():
    checked=[]
    checkedNumbers=[]

    i=0

    for number in theList:

        doing=True

        for checkedNumber in checked:
            if(theList[i]==checkedNumber):
                doing=False
                break

        if doing:
            checking=theList[i]

            j=0
            repeats=0

            for secNumber in theList:
                if(j!=i) and checking==secNumber:
                    repeats+=1

                j+=1

            checked.append(checking)
            checkedNumbers.append(repeats+1)

        i+=1
    i=0

    for number in checked:
        if(checkedNumbers[i]>1):
            print(f"Элемент {number} имеет {checkedNumbers[i]} повторений")

        i+=1

def Task4():
    maxIndex=0
    minIndex=0

    maxNumber=theList[0]
    minNumber=theList[0]

    i=0

    for number in theList:
        if number>maxNumber:
            maxNumber=number
            maxIndex=i
        if number<minNumber:
            minNumber=number
            minIndex=i

        i+=1

    theList[maxIndex]=minNumber
    theList[minIndex]=maxNumber

    print(theList)

def Task5():
    players={"Данил":100,"Сергей":106, "Михаил":8, "Андрей":9,"Павел":5,"Александр":4}
    team={}

    print(f"Все игроки: {players}")

    players=dict(sorted(players.items(), key=lambda x:x[1], reverse=True))


    print("Введите размер комманды")
    membersCount=int(input())

    playersCount=len(players)

    if playersCount==1 or playersCount==2:
        team=players
    elif playersCount==0:
        print("Не из кого выбирать")
    else:
        firstKey=[]
        i=0
        valList=list(players.values())
        keyList=list(players.keys())

        stop=False
          
        for i in range(len(valList)):
            firstMember=valList[i]
            team.clear()

            j=0

            while(j+2<len(valList)):

                    if(firstMember<=(valList[j+1]+valList[j+2])): 
                        team[keyList[j+1]]=valList[j+1]
                        team[keyList[j+2]]=valList[j+2]
                    if(len(team)==membersCount-1):
                        team[keyList[i]]=valList[i]
                        stop=True
                        break

                    j+=1

            if(stop):
                break

            i+=1

    if(len(team)==membersCount):
        skillSumm=0

        teamValueList=list(team.values())

        for player in teamValueList:
            skillSumm+=player

        print(f"Наиболее сплоченная команда: {team}")
        print(f"Сумма ПП = {skillSumm}")
    else:
         print("Состав, удоволетворяющий требованиям не существует")

Task5()