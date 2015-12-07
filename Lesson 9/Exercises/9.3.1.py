# Michael McCullough
# Period 4
# 12/7/15

# 9.3.1

# Grade calculator; gets input of grade in numbers and converts info to a letter value
grade =  float(input("what is a grade in one of your classes? "))

if grade > 0.0 and grade < 0.76:
    print ("You have an F")
elif grade > 0.75 and grade < 1.51:
    print ("You have a D")
elif grade > 1.50 and grade < 2.01:
    print ("You have a C")
elif grade > 2.0 and grade < 2.51:
    print ("You have a B-")
elif grade > 2.50 and grade < 3.01:
    print ("You have a B")
elif grade > 3.0 and grade < 3.51:
    print ("You have an A-")
elif grade > 3.50 or grade <= 4.0:
    print ("You have a solid A!")
else:
    print ("Grade value not found.")
