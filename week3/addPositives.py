## First add all numbers
## Then Add positive numbers

myList = [1,-3,4,2,7,31,46,100, -103, 120]
theSum = 0
sumOfPositives = 0
sumOfNegatives = 0
for number in myList:
    theSum += number
    if number > 0:
        sumOfPositives += number
    else:
        sumOfNegatives += number

print("sum of all numbers", theSum)
print("sum of all positives", sumOfPositives)
print("sum of all negatives", sumOfNegatives)

 

