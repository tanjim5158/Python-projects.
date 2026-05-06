import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]
user_choice = int(input("choose number betwen 0 to 1, 0 for rock, 1 for paper, 2 for scissors: "))
if user_choice>=0 and user_choice <3:
    print(list[user_choice])


computer_choice = random.randint(0, 2)
if computer_choice >=0 and computer_choice <=2:
    print(list[computer_choice])

if user_choice == computer_choice:
    print("its a draw")
elif user_choice >= 3:
    print("you lose")
elif user_choice == 0 and computer_choice ==2:
    print("you win")
elif user_choice >computer_choice:
    print("you win")
else:
    print("you lose")

