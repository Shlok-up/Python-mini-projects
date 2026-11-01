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

