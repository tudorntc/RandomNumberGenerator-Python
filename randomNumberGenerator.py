#Importing a random number

import random

#Max number

userMaxNumber = int(input("Enter the maximum number that can be generated: "))

#Random number generator formula

random_number = random.randint(0, userMaxNumber)

#Displaying the random number

print("Generate number: " + random_number)