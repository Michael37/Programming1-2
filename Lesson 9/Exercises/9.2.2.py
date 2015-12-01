# Michael McCullough
# Period 4
# 11/13/15

# 9.2.2

# This program compares two numbers

num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))

if num1 > num2:
    print ("%d is greater than %d." %(num1, num2))
elif num2 > num1:
    print ("%d is greater than %d" %(num2, num1))
else:
    print ("%d is equal to %d." %(num1, num2))
