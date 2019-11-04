#Sum/Average Program
#Your first and last name: Jefrin Rivera
#Your student ID: s1279110

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

numberlist  = []
for x in range (0,20):
    aNumber = int(input("Enter Number: "))
    numberlist.append(aNumber)
sumint = 0
for x in range (0,20):
    sumint = sumint + numberlist[x]
average = sumint/len(numberlist)
print("The sum is", (sumint))
print("The average is", (average))


