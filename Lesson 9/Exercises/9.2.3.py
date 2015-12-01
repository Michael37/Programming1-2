# Michael McCullough
# Period 4
# 12/1/15

# 9.2.3

# this program guesses a random number

import random

gNum = random.randint (1, 101)
myNum = int(input("Guess what number I'm thinking of between 1 and 100!  "))

if gNum > myNum:
    print ("Your guess was too low :(")
elif myNum > gNum:
    print ("Your guess was too high")
else:
    print ("Congradulations, you guessed correct!")
