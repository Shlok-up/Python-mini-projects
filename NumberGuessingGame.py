#generate a random number
# num=random.random()#random float between 0 to 1
# print(num)
# num=random.randint(1,101)#random number between a to b
# print(num)
# num=random.randrange(1,101)#random range between a to b
# print(num)
# num=random.uniform(1,101)#random float between a to b
# print(num)
#loop {
#ask the user to make a guess(try catch block add to eliminate crash situation)
#if not a valid number
#print error
#if number < guess number
#print too low
#if number >guess number
#print tooo high
#else well done }

import random
number_to_guess=random.randint(1,100)
while(True):
 try:
    guess=int(input("Guess the number between 1 and 100 :"))
    if guess>number_to_guess:#guess is under try bloack so its scope limited
      print("Too High")
    elif guess<number_to_guess:
      print("Too Low")
    else:
      print("Kudos!! You Guessed the number")
      break;
 except ValueError:
    print("Please enter a Valid Number")

