startpop = int(input("Enter the initial population: "))
growthRate = float(input("Enter the rate of growth: "))
growthPeriod = int(input("Enter the number of hours to achieve this rate: "))
totalHours = int(input("Enter the total number of hours during which the population grows: "))
growthCycles = totalHours * growthPeriod
predictedTotal = startpop * (growthRate * growthCycles)
print("The predicted poplation is: ", predictedTotal)
