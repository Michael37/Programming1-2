# Michael McCullough
# Period 4
# 12/2/15

# Lab 9.2

# This program creates a magic 8 "ball"

import random

compNum = random.randint(1, 21)
user = input("Ask me a question. ")

if compNum == 1:
    print ("It's certain!")
elif compNum == 2:
    print ("It is decidedly so.")
elif compNum == 3:
    print ("Without a doubt!")
elif compNum == 4:
    print ("Yes, definitely.")
elif compNum == 5:
    print ("You may rely on it!")
elif compNum == 6:
    print ("As I see it, yes.")
elif compNum == 7:
    print ("Most likely.")
elif compNum == 8:
    print ("Outlook good.")
elif compNum == 9:
    print ("Yas!")
elif compNum == 10:
    print ("Signs point to yes.")
elif compNum == 11:
    print ("Reply hazy; try again later.")
elif compNum == 12:
    print ("Ask again later.")
elif compNum == 13:
    print ("Better to not tell you now. :)")
elif compNum == 14:
    print ("Cannot predict now.")
elif compNum == 15:
    print ("Concentrate and ask again.")
elif compNum == 16:
    print ("Don't count on it.")
elif compNum == 17:
    print ("My reply is no.")
elif compNum == 18:
    print ("My sources say no.")
elif compNum == 19:
    print ("Outlook not so good.")
else:
    print ("Very doubtful.")
