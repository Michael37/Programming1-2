# Michael McCullough
# Period 4
# 12/8/15

# 9.3.2

age = float(input("How old are you? "))

if age < 11:
    print ("You're a little one.")
elif age > 10 and age < 21:
    print ("Getting done with school!")
elif age > 20 and age < 31:
    print ("Wow, starting a carrer, cool.")
elif age > 30 and age < 41:
    print ("Give your work your all, bro!")
elif age > 41 and age < 50:
    prin ("Getting done with your carrer.")
elif age > 50:
    carrer = input("Retired yet? ")

if carrer == "yes":
    print ("Congrats!")
elif carrer == "no":
    print ("It's not too late!")
else:
    print ("Error 404: Value Not Found")
