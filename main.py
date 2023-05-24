try:
    bacteriaCount = float(input('Enter initial count of bacteria: '))
    numHours = int(input('Enter the number of hours: '))

    hoursToTime = numHours * 60
    genTime = hoursToTime / 20
    num = numHours ** genTime

    print("")

    binaryFission = bacteriaCount * num
    print("The number of bacteria per hour will be:")

    hour = "Hour "
    for x in range(1,6):
        value = hour + str (x) + " = " + ""
        bacteriaPerHour = x * num
        floatToString = str (bacteriaPerHour)
        print(value + floatToString)
except ValueError:
    print("Error! Number Only.")
except OverflowError:
    print("Please input correct hours!")
