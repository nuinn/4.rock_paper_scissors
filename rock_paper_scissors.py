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

options = [rock, paper, scissors]
print('What will you play?')
choice = int(input('Choose 0 for Rock, 1 for Paper and 2 for Scissors!\n'))
print(f"You chose: {options[choice]}")
computer_choice = random.randint(0, len(options) - 1)
print(f"Computer chose: {options[computer_choice]}")
differential = choice - computer_choice
if choice == computer_choice:
    print("It's a draw!")
elif differential == 1 or differential == -2:
    print("You win!")
else:
    print("You lose, sucker!")
