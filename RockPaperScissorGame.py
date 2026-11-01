import random
while(True):
 user_choice=input('Rock,Paper,or Scissors? (r/p/s)').lower()
 choices=('r','p','s')
# if user_choice != 'r' and user_choice != 'p' and user_choice != 's':
 emojis={
    'r':"🪨",
    's':"✂️",
    'p':"📃",
 }
 if user_choice not in choices:
    print("Invalid Choice !")
    continue;#if invalid cjoice is made it will run next code as well but continue will skip all further steps and starts from beginning
 comp_choice=random.choice(choices)
 print(f"You Chose :{emojis[user_choice]}")
 print(f"Computer Chose :{emojis[comp_choice]}")

 if user_choice==comp_choice:
    print("Tie!")
 elif ((user_choice =='r' and comp_choice=='s')or(user_choice =='p' and comp_choice=='r')or(user_choice =='s' and comp_choice=='p')):
    print("You Won!! , Computer Lose")
 else:
    print("Computer Won , You Lose")

 should_continue=input("Want to continue(Y/N)?").lower
 if should_continue=="n":
    print("Thank You for playing")
    break;