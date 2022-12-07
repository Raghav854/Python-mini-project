def leapYears(start, end):
    startDate = start.split('/')
    endDate = end.split('/')
    startYear = int(startDate[2])
    endYear = int(endDate[2])

    leapYear = []
    nonLeapYear = []
    for i in range(startYear, endYear+1):
        if (i % 400 == 0 or i%100 !=0) and i % 4 == 0:
            leapYear.append(i)
        else:
            nonLeapYear.append(i)
    print("Leap Years: ", end = "")
    for j in range(len(leapYear)):
        if j == len(leapYear)-1:
            print(leapYear[j], end = ".")
            print()
        else:
            print(leapYear[j], end=', ')
    print("Non Leap Years: ", end = "")
    for k in range(len(nonLeapYear)):
        if k == len(nonLeapYear)-1:
            print(nonLeapYear[k], end=".")
            print()
        else:
            print(nonLeapYear[k], end =', ')
start = input("Enter start date: ")
end = input("Enter end date: ")
leapYears(start, end)