# Michael McCullough
# Period 4
# 12/11/15

# Age Calculator

age = int(input("How old are you? "))

days = age*365
hours = days*24
minutes = hours*60
seconds = minutes*60

print ("You've lived %d days," %(days))
print ("%d hours," %(hours))
print ("%d minutes" %(minutes))
print ("or %d seconds!" %(seconds))
